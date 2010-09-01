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
    if request.user.is_authenticated():
        print "user %s is authenticated \n" %(request.user.username)
        student=request.user
        profile=UserProfile.objects.get(user=student)
        return {'student' : student, 'profile' : profile, }
    else:
        print "user is NOT authenticated\n"
        return {}
 

def get_public_videos(request):
    MAX_DISPLAY=5
#    lab_records = Student.labrecord_set.order_by('lab__num')
    quizzes = PublicVideo.objects.filter(type='OldQuiz')[:MAX_DISPLAY]
    labs = PublicVideo.objects.filter(type='LabHint')[:MAX_DISPLAY]
    concepts = PublicVideo.objects.filter(type='Concept')[:MAX_DISPLAY]
    tutprobs = PublicVideo.objects.filter(type='TutProb')[:MAX_DISPLAY]
# located in views.py

    dict = {
        'quizzes': quizzes,
        'labs':labs,
        'concepts': concepts,
        'tutprobs': tutprobs,
        }
    return dict

def get_student_favorites(request):
    MAX_DISPLAY=5
    student_dict= get_student_info(request)
    profile = student_dict['profile']
    fav_quizzes = profile.favorites.filter(type='OldQuiz')[:MAX_DISPLAY]
    fav_labs = profile.favorites.filter(type='LabHint')[:MAX_DISPLAY]
    fav_concepts = profile.favorites.filter(type='Concept')[:MAX_DISPLAY]
    fav_tutprobs = profile.favorites.filter(type='TutProb')[:MAX_DISPLAY]
    
    dict = {
        'fav_quizzes': fav_quizzes,
        'fav_labs': fav_labs,
        'fav_concepts': fav_concepts,
        'fav_tutprobs': fav_tutprobs,
        }  
    dict.update(student_dict)
    return dict

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


## use built in decorator to limit access to logged in users
@login_required
def student_portal(request):
    public_dict = get_public_videos(request)
    favorite_dict = get_student_favorites(request)
    template = "student_portal.html"
    return render_to_response(template, public_dict, 
                              context_instance=
                              RequestContext(request, processors=[get_student_favorites]))


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

#                              context_instance=
#                              RequestContext(request, processors=[get_student_info]))


def browse(request, topic_snippet_id=23, is_favorite='False', query_string=''):

    all_topic_assignments = TopicAssignment.objects.all()

    ta_id = int(topic_snippet_id)
    print "ta_id = %d\n" %(ta_id)
    selected_ta = all_topic_assignments.get(pk=ta_id)
    selected_video = selected_ta.video
    v_id = selected_video.id

    favorite_bool=False
    if is_favorite=='True':
        favorite_bool=True

    all_videos=PublicVideo.objects.all()
    selected_video = all_videos.get(pk=v_id)
    print "vid is %d" %(v_id)

    if 'QUERY_STRING' in request.META.keys():
        query_string='?'+request.META['QUERY_STRING']   
    query=query_string
    print "full_path = %s\n" %(query)
 
    favoriter_set = selected_ta.userprofile_set.all()   
    if request.user:
        if request.user.is_authenticated():
            if favoriter_set.filter(user=request.user).count():
                favorite_bool=True
                
    filterset=TopicAssignmentFilterSet(request.GET, queryset=TopicAssignment.objects.all())

    print "favorite_bool= %s and is_favorite=%s \n" %(favorite_bool, is_favorite)

    if favorite_bool:
        is_favorite=u'True'
    else:
        is_favorite=u'False'

    dict={
        'query_string':query,
        'is_favorite':is_favorite,
        'all_videos':all_videos,
        'all_topic_assignments':filterset,
        'selected_ta':selected_ta,
        }

    template="browse.html"
    response = render_to_response(template, dict)
#    print "the outgoing response is %s\n" %(response.content)
    return response
    
                                           








@login_required
def show_media(request, public_video_id):
    media_object= PublicVideo.objects.get(pk=public_video_id)
    template = "show_to_student.html"
    this_dict = {'media': media_object,}

    return render_to_response(template, this_dict,
                              context_instance = RequestContext(request)) 
