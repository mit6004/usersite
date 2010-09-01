from tutorials import loader
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from tutorials.models import *
from django.contrib.auth.decorators import login_required
from tutorials.forms import PublicVideoForm



def check_staff(request):
    if not request.user:
        return HttpResponseRedirect('accounts/login/')
    if not request.user.is_staff:
        return HttpResponseRedirect('accounts/login/')
    

@login_required
def preview_and_set_topic(request, video_id):
    for item in request.POST.keys():
        print "request.POST[%s] = %s\n" %(item, request.POST[item])
    #check_staff(request)

    topic_choices = [ [topic[0], topic[1]] for topic in TOPIC_CHOICES]

    video_id=int(video_id)
    video = PublicVideo.objects.get(pk=video_id)

    if request.method=="POST":
        print "post!"

        if 'start_time_units' in request.POST.keys():
            start_time_units = request.POST['start_time_units']
        else: start_time_units = 0

        if 'stop_time_units' in request.POST.keys(): 
            stop_time_units = request.POST['stop_time_units']
        else: stop_time_units = 0

        if 'topic_name' in request.POST.keys(): 
            topic = request.POST['topic_name']
        else: topic=''
        print "topic is %s\n" %(topic)
        
        ta = TopicAssignment(video = video, 
                             start_time = start_time_units, 
                             stop_time = stop_time_units,
                             topic = topic)
        ta.save()
        return HttpResponseRedirect('/upload_video/')
    else:
        ta = TopicAssignment(video=video)

    dict = {
        'video': video,
        'topic_choices': topic_choices,
            }
    template="movie_preview.html"
    return render_to_response(template, dict)


@login_required
def upload_video(request):

    # makes sure that the user is staff before rendering the page
    check_staff(request)

    if request.method=="POST":
        video_form = PublicVideoForm(request.POST, request.FILES)
        if not video_form.is_valid():
            template="<h2> Please check the form submission and try again </h2>"
            return render_to_response(template, {})
        else:
            video = video_form.save(commit=False)
            file = request.FILES['file']
            video.file=file
            print "video.file.name = %s" %(video.file.name)
            print "file name is %s" %(file.name)
            video.save()
            return HttpResponseRedirect('/topic_assign/%d/' %(video.id) )
    else:
        video_form = PublicVideoForm()
    dict = { 
        'user':request.user,
        'video_form':video_form,
        }
    template = 'upload_video.html'
    return render_to_response(template, dict)
