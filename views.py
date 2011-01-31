from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from records.models import *
from tutorials.models import TopicAssignment, ViewInterval
from staff_views import get_img_url

from tutorials.filters import TopicAssignmentFilterSet
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.template import RequestContext
from django.db.models import Q
from django.conf import settings

from django.utils import simplejson
from django.core import serializers

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


def get_student_favorites(request):
    MAX_DISPLAY=5
    student_dict= get_student_info(request)
    
    if student_dict['is_authenticated']:
        profile = student_dict['profile']
        faves = profile.favorite_set.all()
    else:
        faves = TopicAssignment.objects.none()

    dict = {
        'faves':faves,
        }  
    dict.update(student_dict)
    return dict


def render_with_student_context(request, template, dict):    
    return render_to_response(template, dict, 
                              context_instance=
                              RequestContext(request, processors=[get_student_favorites]))



def show_by_topic(request, topic):
    topic_assignments = TopicAssignment.objects.filter(topic=topic)
    title_string='List of Snippets About %s' %(topic)
    dict = {
        'title_string': title_string,
        'header_string': title_string,
        'ta_query_set': topic_assignments,
        }
    template="topic_assignment_list.html"
    return render_with_student_context(request, template, dict)
                   

def show_by_author(request, author_username):
    topic_assignments = TopicAssignment.objects.filter(video__author__username=author_username)
    title_string='List of Snippets by %s' %(author_username)
    dict = {
        'title_string': title_string,
        'header_string': title_string,
        'ta_query_set': topic_assignments,
        }
    template="topic_assignment_list.html"
    return render_with_student_context(request, template, dict)

def show_by_semester(request, semester):
    topic_assignments = TopicAssignment.objects.filter(video__semester=semester)
    title_string='List of Snippets from %s' %(semester)
    dict = {
        'title_string': title_string,
        'header_string': title_string,
        'ta_query_set': topic_assignments,
        }
    template="topic_assignment_list.html"
    return render_with_student_context(request, template, dict)

def show_by_type(request, type):
    topic_assignments = TopicAssignment.objects.filter(video__type=type)
    title_string='List of %s Snippets' %(type)
    dict = {
        'title_string': title_string,
        'header_string': title_string,
        'ta_query_set': topic_assignments,
        }
    template="topic_assignment_list.html"
    return render_with_student_context(request, template, dict)


def make_comment(request, user, topic_assignment):
    permissions='students'
    if 'permissions' in request.POST.keys():
        permissions = request.POST['permissions']
    
    text=""
    if 'text' in request.POST.keys():
        text = request.POST['text']
    if not (text == "Write your comment here...."):    
        comment=Comment(text=text, permissions=permissions)
        comment.clip=topic_assignment
        comment.user=user
        comment.save()
        print "saved comment %s by %s \n" %(comment.text, comment.user.username)


def add_favorite(request, profile, ta):
    # ADDED LINE TO CONSTRUCT FAVORITE MODEL INSTANCE 9/8/10
    favorite=Favorite()
    favorite.profile=profile
    favorite.ta=ta
    favorite.save()

def rm_favorite(request, profile, ta):
    f = Favorite.objects.filter(ta=ta).filter(profile=profile)
    f.all().delete()


# main page for displaying a single movie with comment and favorite options
def show_media(request, ta_id):
    ta_id = int(ta_id)
    ta = TopicAssignment.objects.get(pk=ta_id)
    linked_problems=LinkedWebPage.objects.filter(topic_assignment__id=ta_id)
    print "got ta with topic = %s\n" %(ta.topic)
    print "got ta with src = %s\n" %(ta.video.get_absolute_url())
    template="show_media.html"

    is_user_favorite=False
    student = AnonymousUser()
    student_info = get_student_info(request)
    # get the profile and authentication info

    comments=Comment.objects.none()
#    comments=ta.comments.all()
    print "there are %d comments  before filtering \n" %(comments.count())
   # empty query set
    if student_info['is_authenticated']:
        student=student_info['student']
        student_faves = get_student_favorites(request)

        comments = ta.comments.filter(
            Q(permissions='students') 
            | ( Q(permissions='staff') & Q(user=student) ) )
        if student.is_staff:
            comments=ta.comments.all()

        if student_faves['faves'].filter(pk=ta_id).count():
            is_user_favorite=True
    
        if request.method=='POST':
            if 'submit_comment' in request.POST.keys():
                make_comment(request, student, ta)
            if 'add_favorite' in request.POST.keys():
                add_favorite(request, student_info['profile'], ta)
            if 'rm_favorite' in request.POST.keys():
                rm_favorite(request, student_info['profile'], ta)
            
            for key in request.POST.keys():
                print "requst.POST[%s] = %s \n" %(key, request.POST[key])
                

    print "there are %d comments \n" %(comments.count())    
    print "user.is_authenticated = %s \n" %(request.user.is_authenticated())

    topic_number=TOPIC_NUMBERS[ta.topic]
    dict = {
        'debug': True,
        'selected_ta':ta,
        'topic':ta.topic,
        'linked_problems':linked_problems,
        'is_user_favorite':is_user_favorite,
        'user': student,
        'comments': comments,
        'permissions': ['staff','student'],
        }
    return render_with_student_context(request, template, dict)


def landing(request):
    template="topic_list.html"
    dict={}
    return render_with_student_context(request, template, dict)



def tutorial_main(request):
    template = "tutprobs.htm"
    dict = {}
    return render_to_response(template, dict)



##def tutorial_by_topic(request, topic):
##    print "\n in XFtutorial_by_topic\n"
##    # make sure right format for dictionary above
##    base_url = "http://6004.csail.mit.edu/currentsemester/tutprobs/"
##    base_url="tutprobs"
##    page = TUTORIAL_PROBLEM_URLS[topic]
##    direct_to = base_url + page
##    print "redirecting from tutorial by topics for topic=%s to %s\n" %(topic, direct_to)
##    return HttpResponseRedirect(direct_to)


def tutorial_by_topic(request, topic):
    print "in views.tutorial_by_topic"
    template="%s" %(topic)
    print "topic is %s \n" %(topic)
    dict = {}
    return render_to_response(template, dict)

## shows the tutorial problems for the topic assigned to this clip
## want to refine to break this up by problem.
def tutorial_by_id(request, topic, linked_problem_id):
    print "\n in tutorial_by_id\n"
    base_url = "http://6004.csail.mit.edu/currentsemester/tutprobs/"
    page = TUTORIAL_PROBLEM_URLS[topic]
    lp_id = int(linked_problem_id)
    lp = LinkedWebPage.objects.get(pk=lp_id)
    lp_pointer = lp.pointer_on_page
    direct_to = base_url + page + lp_pointer
    print "redirecting from tutorial by id for id=%d to %s\n" %(lp_id, direct_to)
    return HttpResponseRedirect(direct_to)


## testing jquery ##
## server side handler function 
def post_handler(request):
    print "In post_handler \n"
    
    message = 'failure'
    interval = ViewInterval()
    if request.is_ajax():
        print "request in post handler is ajax \n"
        if request.method == 'POST':
            
            iform_start = request.POST['iform_start']
            print "iform_start : %s" %(iform_start)
            iform_end = request.POST['iform_end']
            print "iform_end : %s" %(iform_end)
            username = request.POST['user']
            user = User.objects.get(username=username)
            print "user : %s" %(user)
            ta_id = int(request.POST['ta_id'])
            print "ta_id : %s" %(ta_id)
            ta = TopicAssignment.objects.get(pk=ta_id)
            print "ta : %s" %(ta)
            img_url = get_img_url(ta_id)
            img_div = "<div id=\"view_graph_div\" class=\"view_graph_div\" style=\"float:left;align:left\">"
            img_div = img_div + "<img id=\"view_graph\" name=\"view_graph\" src=\"" + img_url + "\" />"
            img_div = img_div + "</div>"
            message = img_div
            ##interval = ViewInterval(ta=ta, user=user, start_time=iform_start, end_time=iform_end)
            interval = ViewInterval()
            print "made an interval"
            interval.ta = ta
            interval.user=user
            interval.start_time = iform_start
            interval.stop_time = iform_end
            interval.save()
            
            #print "about to run serializer"
            #data_dict = serializers.serialize("json", interval)
    #print "about to return http response: %s  \n" %(data_dict)
    print "saved interval"
    return HttpResponse(message, mimetype="text/html")

    
def post_test(request):
    template = "js_test.html"
    ta_id = 4
    ta = TopicAssignment.objects.get(pk=ta_id)
    linked_problems=LinkedWebPage.objects.filter(topic_assignment__id=ta_id)
    is_user_favorite=False
    student = AnonymousUser()
    student_info = get_student_info(request)
    # get the profile and authentication info
    comments=Comment.objects.none()
#    comments=ta.comments.all()

   # empty query set   
    if student_info['is_authenticated']:
        student=student_info['student']
        student_faves = get_student_favorites(request)
        comments = ta.comments.filter( Q(permissions='students') 
                                       | ( Q(permissions='staff') & Q(user=student) ) )
        if student.is_staff:
            comments=ta.comments.all()
        if student_faves['faves'].filter(pk=ta_id).count():
            is_user_favorite=True
        if request.method=='POST':
            if 'submit_comment' in request.POST.keys():
                make_comment(request, student, ta)
            if 'add_favorite' in request.POST.keys():
                add_favorite(request, student_info['profile'], ta)
            if 'rm_favorite' in request.POST.keys():
                rm_favorite(request, student_info['profile'], ta)
            for key in request.POST.keys():
                print "requst.POST[%s] = %s \n" %(key, request.POST[key])
    topic_number=TOPIC_NUMBERS[ta.topic]
    dict = {
        'debug': True,
        'selected_ta':ta,
        'topic':ta.topic,
        'linked_problems':linked_problems,
        'is_user_favorite':is_user_favorite,
        'user': student,
        'comments': comments,
        'permissions': ['staff','student'],
        }
    return render_with_student_context(request, template, dict)
