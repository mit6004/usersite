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
    print "topic_assignments (by topic) size = %s\n" %(topic_assignments.count())
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
    print "got ta with topic = %s\n" %(ta.topic)
    print "got ta with src = %s\n" %(ta.video.get_absolute_url())
    template="show_media.html"
    dict = {
        'ta':ta,
        }
    return render_to_response(template, dict)
    
