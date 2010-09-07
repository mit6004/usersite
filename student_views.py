from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from records.models import *
from tutorials.models import *

from tutorials.filters import TopicAssignmentFilterSet
from django.contrib.auth.decorators import login_required

from django.template import RequestContext

from django.conf import settings
import datetime, os, re




def get_student_info(request):
    is_authenticated=request.user.is_authenticated()
    
    if is_authenticated:
        print "user %s is authenticated \n" %(request.user.username)
        student=request.user
        profile=UserProfile.objects.get(user=student)
        return {'student' : student, 
                'profile' : profile,
                'is_authenticated': is_authenticated,
                }
    else:
        print "user is NOT authenticated\n"
        return {'is_authenticated':is_authenticated}
 

def get_public_videos(request):
    MAX_DISPLAY=5
#    lab_records = Student.labrecord_set.order_by('lab__num')
    quizzes = TopicAssignment.objects.filter(video__type='OldQuiz')
    labs = TopicAssignment.objects.filter(video__type='LabHint')
    concepts = TopicAssignment.objects.filter(video__type='Concept')
    tutprobs = TopicAssignment.objects.filter(video__type='TutProb')
    all_vids = TopicAssignment.objects.all()
# located in views.py

    dict = {
        'quizzes': quizzes,
        'labs':labs,
        'concepts': concepts,
        'tutprobs': tutprobs,
        'all_vids':all_vids,
        }
    for key in dict.keys():
        print "dict[%s] : %s\n" %(key, dict[key])
    return dict


def get_student_favorites(request):
    MAX_DISPLAY=5
    student_dict= get_student_info(request)
    profile = student_dict['profile']
    fav_quizzes = profile.favorites.filter(video__type='OldQuiz')
    fav_labs = profile.favorites.filter(video__type='LabHint')
    fav_concepts = profile.favorites.filter(video__type='Concept')
    fav_tutprobs = profile.favorites.filter(video__type='TutProb')
    faves = profile.favorites.all()
    dict = {
        'fav_quizzes': fav_quizzes,
        'fav_labs': fav_labs,
        'fav_concepts': fav_concepts,
        'fav_tutprobs': fav_tutprobs,
        'faves':faves,
        }  
    dict.update(student_dict)
    return dict



def get_faves_by_topic(request):
    student_dict=get_student_info(request)
    student_faves = student_dict['profile'].favorites.all()
    topic_choices = [ [topic[0], topic[1]] for topic in TOPIC_CHOICES]
    faves_by_topic={}
    for topic_tuple in topic_choices:
        topic_faves = student_faves.filter(topic=topic_tuple[0])
        ## get all TopicAssigned video clips that match the exact topic part
        entry=''
        for topic_fave in topic_faves:
            entry = '%s <td><a href=\"%s\">%s</a></td>' %(entry, 
                                                     topic_fave.video.get_absolute_url(), 
                                                     topic_fave.video.file_name)
        faves_by_topic[topic_tuple[1]]=entry
        print "faves_by_topic[%s]: %s\n" %(topic_tuple[1], faves_by_topic[topic_tuple[1]])
    return faves_by_topic





@login_required
def preview_and_set_topic(request, video_id):

    for item in request.POST.keys():
        print "request.POST[%s] = %s\n" %(item, request.POST[item])

    if not request.user:
        html = "<h2> Error: you are not <a href=\"accounts/login.html\">logged in.</a></h2>"
        return render_to_response(html, {})
    if not request.user.is_staff:
        html = "<h2> Error: you are not <a href=\"accounts/login.html\">logged in as staff.</a></h2>"
        return render_to_response(html, {})

    video_id=int(video_id)
    video = PublicVideo.objects.get(pk=video_id)
    dict = {
        'video':video,
        }
    template="movie_preview.html"
    return render_to_response(template, dict)



## Main view for media browser
## use built in decorator to limit access to logged in users
@login_required
def student_portal(request, topic_snippet_id=1, is_favorite='False', show='Favorites', query_string=''):
    public_ta_dict = get_public_videos(request)
    favorite_ta_dict = get_student_favorites(request)
    faves_by_topic = get_faves_by_topic(request)
    ta_id = int(topic_snippet_id)
    all_topic_assignments=public_ta_dict['all_vids']
    selected_ta = all_topic_assignments.get(pk=ta_id)

    if 'QUERY_STRING' in request.META.keys():
        query_string='?'+request.META['QUERY_STRING']   
    query=query_string
     
    is_favorite=u'False'    
    if favorite_ta_dict['faves'].filter(pk=ta_id):
        is_favorite=u'True'

    verbose_topics = [ topic[1] for topic in TOPIC_CHOICES ]

    pre_filter = TopicAssignment.objects.all()
    if show=='Favorites':
        pre_filter=favorite_ta_dict['faves']
    # only show a student's favorites
    filterset=TopicAssignmentFilterSet(request.GET, queryset=pre_filter)
    dict={
        'query_string':query,
        'is_favorite':is_favorite,
        'all_topic_assignments':filterset,
        'selected_ta':selected_ta,
        'verbose_topics':verbose_topics,
        'faves_by_topic':faves_by_topic,
        'show': show,
        }
    for key in dict.keys():
        print "dict[%s] : %s\n" %(key, dict[key])
#    template="student_browse.html"
    template="browse.html"
    return render_to_response(template, dict, 
                              context_instance=
                              RequestContext(request, processors=[get_student_favorites]))

## public browser. no authentication or favoriting.
def browse(request, topic_snippet_id=1, query_string=''):
    all_topic_assignments = TopicAssignment.objects.all()
    ta_id = int(topic_snippet_id)
    print "ta_id = %d\n" %(ta_id)
    selected_ta = all_topic_assignments.get(pk=ta_id)
    selected_video = selected_ta.video
    v_id = selected_video.id

    all_videos=PublicVideo.objects.all()
    selected_video = all_videos.get(pk=v_id)
    print "vid is %d" %(v_id)

    if 'QUERY_STRING' in request.META.keys():
        if not request.META['QUERY_STRING'] =='':
            query_string='?'+request.META['QUERY_STRING']   
    query=query_string
    print "full_path = %s\n" %(query)
 
    filterset=TopicAssignmentFilterSet(request.GET, queryset=TopicAssignment.objects.all())

    dict={
        'query_string':query,
        'all_videos':all_videos,
        'all_topic_assignments':filterset,
        'selected_ta':selected_ta,
        }

    template="browse.html"
    response = render_to_response(template, dict)
#    print "the outgoing response is %s\n" %(response.content)
    return response
    
                                           






## not used. for testing.


def media_browser(request):
    all_videos = PublicVideo.objects.all()
    v_id=3
    # for now, this is "Timothy Leary's Calenday App - one of the smaller ones.
    print "vid is %d" %(v_id)
    all_topic_assignments = TopicAssignment.objects.all()

    staff_faves={}
    all_faves={}

    # -- stuff to keep the right video-topic thing selected when 
    # -- the filter list is modified 
    query_string=request.META['QUERY_STRING']
    print "query_string = %s\n" %(query_string)
    v_id_field = 'v_id' in request.GET.keys()
    start_char=u'?'
    full_path=''
    if v_id_field:
        v_id=request.GET['v_id']
    full_path=re.sub("\?*v_id=[^&]*", '', request.get_full_path())
    if 'topic' in request.GET.keys():
        full_path=re.sub("\&*v_id=[^&]*", '', request.get_full_path())
        start_char=u'&'
    # -- end silly query string processing stuff
    
    selected_video = all_videos.get(pk=v_id)
    print "full_path = %s\n" %(full_path)
    
    for k in request.GET.keys():
        print "request.GET[%s] = %s\n" %(k, request.GET[k])
            
    for video in all_videos:
        favoriter_set = video.userprofile_set.all()
        staff_faves[video.id]=favoriter_set.filter(user__is_staff=True).count()
        all_faves[video.id]=favoriter_set.count()
    
    filterset=TopicAssignmentFilterSet(request.GET, queryset=TopicAssignment.objects.all())

    dict={
        'full_path':full_path,
        'start_char': start_char,
        'all_topic_assignments':filterset,
        'selected_video':selected_video,
        'staff_faves':staff_faves,
        'all_faves':all_faves,
        }

    template="browse.html"
    response = render_to_response(template, dict)
    print "the outgoing response is %s\n" %(response.content)
    return response
