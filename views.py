from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from records.models import *
from tutorials.models import TopicAssignment

from tutorials.filters import TopicAssignmentFilterSet
from django.contrib.auth.decorators import login_required

from django.template import RequestContext

from django.conf import settings
import datetime, os, re



def show_by_topic(request, topic):
    topic_assignments = TopicAssignment.objects.filter(topic=topic)

    dict = {
        'ta_query_set': topic_assignments,
        }
    template="topic_assignment_list.html"
    return render_to_response(template, dict)

def show_by_author(request, author_username):
    topic_assignments = TopicAssignment.objects.filter(video__author__username=author_username)
    
    dict = {
        'ta_query_set': topic_assignments,
        }
    template="topic_assignment_list.html"
    return render_to_response(template, dict)

def show_by_semester(request, semester):
    topic_assignments = TopicAssignment.objects.filter(video__semester=semester)
    
    dict = {
        'ta_query_set': topic_assignments,
        }
    template="topic_assignment_list.html"
    return render_to_response(template, dict)

def show_by_type(request, type):
    topic_assignments = TopicAssignment.objects.filter(video__type=type)
    
    dict = {
        'ta_query_set': topic_assignments,
        }
    template="topic_assignment_list.html"
    return render_to_response(template, dict)


def show_media(request, ta_id):
    ta_id = int(ta_id)
    ta = TopicAssignment.objects.get(pk=ta_id)
    linked_problems=LinkedWebPage.objects.filter(topic_assignment__id=ta_id)
    print "got ta with topic = %s\n" %(ta.topic)
    print "got ta with src = %s\n" %(ta.video.get_absolute_url())
    template="show_media.html"
    topic_number=TOPIC_NUMBERS[ta.topic]
    dict = {
        'ta':ta,
        'topic_number':topic_number,
        'linked_problems':linked_problems,
        }
    return render_to_response(template, dict)


def tutorial_by_topic(request, topic):
    print "\n in tutorial_by_topic\n"
    # make sure right format for dictionary above
    base_url = "http://6004.csail.mit.edu/currentsemester/tutprobs/"
    page = TUTORIAL_PROBLEM_URLS[topic]
    direct_to = base_url + page
    print "redirecting from tutorial by topics for topic=%s to %s\n" %(topic, direct_to)
    return HttpResponseRedirect(direct_to)


def tutorial_by_id(request, topic, linked_problem_id):
    print "\n in tutorial_by_id\n"
    base_url = "http://6004.csail.mit.edu/currentsemester/tutprobs/"
    page = TUTORIAL_PROBLEM_URLS[topic]
    lp_id = int(linked_problem_id)
    lp = LinkedWebPage.objects.get(pk=lp_id)
    lp_pointer = lp.pointer_on_page
    direct_to = pase_url + page + lp_pointer
    print "redirecting from tutorial by id for id=%d to %s\n" %(lp_id, direct_to)
    return HttpResponseRedirect(direct_to)



    
