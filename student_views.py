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
        print "user % is authrnticated \n" %(request.user)
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

    query_string=request.META['QUERY_STRING']
    print "query_string = %s\n" %(query_string)
    v_id_field = 'v_id' in request.GET.keys()



        #then we know the other form has been submitted before.

    start_char=u'?'
    full_path=''
    if v_id_field:
        v_id=request.GET['v_id']
    
    full_path=re.sub("\?*v_id=[^&]*", '', request.get_full_path())
    if 'topic' in request.GET.keys():
        full_path=re.sub("\&*v_id=[^&]*", '', request.get_full_path())
        start_char=u'&'
    
    selected_video = all_videos.get(pk=v_id)
    print "full_path = %s\n" %(full_path)
    
    for k in request.GET.keys():
        print "request.GET[%s] = %s\n" %(k, request.GET[k])
            
    for video in all_videos:
        favoriter_set = video.userprofile_set.all()
        staff_faves[video.id]=favoriter_set.filter(user__is_staff=True).count()
        all_faves[video.id]=favoriter_set.count()
    
    prefiltered=TopicAssignment.objects.all()

##    if not topic=='':
##        prefiltered=prefiltered.filter(topic=topic)
##    if not author=='':
##        prefiltered=prefiltered.filter(video__author=author)
##    if not type=='':
##        prefiltered=prefiltered.filter(video__type=type)
##    if not semester=='':
##        prefiltered=prefiltered.filter(video__semester=semester)
    
    filterset=TopicAssignmentFilterSet(request.GET, queryset=prefiltered)

    dict={
        'full_path':full_path,
        'start_char': start_char,
        'all_topic_assignments':filterset,
        'selected_video':selected_video,
        'staff_faves':staff_faves,
        'all_faves':all_faves,
        }
    
    template="browse.html"
    return render_to_response(template, dict)




#                              context_instance=
#                              RequestContext(request, processors=[get_student_info]))


@login_required
def show_media(request, public_video_id):
    media_object= PublicVideo.objects.get(pk=public_video_id)
    template = "show_to_student.html"
    this_dict = {'media': media_object,}

    return render_to_response(template, this_dict,
                              context_instance = RequestContext(request)) 
