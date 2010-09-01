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
    pass

@login_required
def preview_and_set_topic(request, video_id):
    for item in request.POST.keys():
        print "request.POST[%s] = %s\n" %(item, request.POST[item])
    check_staff(request)



    video_id=int(video_id)
    video = PublicVideo.objects.get(pk=video_id)
    dict = {'video':video,}
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
