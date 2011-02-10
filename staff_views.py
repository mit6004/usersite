from tutorials import loader
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from tutorials.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
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
        # We have an upload submission from movie_preview.html
        print "post!"

        if 'start_time_units' in request.POST.keys():
            # then the button, with input type "onclick" triggers the event listener 
            # in movie_preview.html "set_start_time();" and here, this the dictionary below, 
            # we have the conversion from start_time_units to start_time in the 
            # topic_assignment object itself. 
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
def select_video_for_assignment(request):
    check_staff(request)

    if request.method=="POST":
        v_id = request.POST['selected_video']
        print "selected video # %s chosen for topic assignment \n" %(v_id)
        vid = int(vid)
        video = PublicVideo.objects.get(pk=vid)
        topic_choices = [ [topic[0], topic[1]] for topic in TOPIC_CHOICES]
        template = "movie_preview.html"
        dict = { 'video': video, 'topic_choices': topic_choices, }
        return render_to_response(template, dict)

    videos = PublicVideo.objects.all()
    dict = { 'videos': videos }
    template = "select_video_for_assignment.html"
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


def display_interval_list(request):
    topic_assignments = TopicAssignment.objects.all()
    title_string = "List of Topic-Assigned Clips"
    header_string = "Click one of the links to check the view history"
    dict = {
        'title_string' : title_string,
        'header_string' : header_string,
        'ta_query_set' : topic_assignments
        }
    template = "view_history_list.html"
    return render_to_response(template, dict)



def get_img_url(ta_id, x_length="0"):
    print "(get_img_url)"
    id=int(ta_id)
    ta = TopicAssignment.objects.get(pk=id)
    #print "(display_interval_views) ta = %s" %(ta)
    intervals = ta.viewinterval_set.all()
    number = intervals.count()
    interval_stop_times = intervals.values_list('stop_time', flat=True).order_by('-stop_time')
    if not (interval_stop_times.count() == 0):
        intervals_max = int(interval_stop_times[0])
    else:
        intervals_max = 100
    
    x_length = int(x_length)
    if (x_length == 0):
        x_length = intervals_max
    
    #print "x_length = " + str(x_length)
    #print "intervals_max = " + str(intervals_max)
    #print "(display_interval_views) there are %d intervals for this topic assignment." %(number)
    view_vector = [0]
    for i in range(intervals_max):
        #print "in outer for loop with index = " + str(i)
        view_vector.append(0)
        # initialize array value for this index to zero
        for interval in intervals:
            if interval.has_second(i):
                #print "view_vector["+str(i)+"] = " + str(view_vector[i])
                view_vector[i] = view_vector[i] + 1

    #for i in range (intervals_max):
    #    print "-- view_vector["+str(i)+"] = " + str(view_vector[i])
    max_views = max(view_vector)
    if (max_views == 0):
        max_views = 1

    #print "max_views = " + str(max_views)
    img_url = "http://chart.googleapis.com/chart?"
    # to make a line chart
    img_url = img_url + "cht=lc&"
    # make a graph that is 800x300 (default)
    img_url = img_url + "&chs=600x300"
    # add the data values
    img_url = img_url + "&chd=t:" + str(view_vector[0]*100/max_views)
    for i in range (1, intervals_max):
        img_url = img_url + ","+ str(view_vector[i]*100/max_views)
    # format the axis scale and color, respectively
    img_url = img_url + "&chxt=x,y&chxr=0,0," + str(x_length) + "," + str(x_length/10) +"|1,0,"+str(max_views)+",1"
    img_url = img_url + "&chxs=0,2244FF,12,0,lt|1,0055FF,10,1,lt"

    return img_url


# want to count all of the people viewing at each time unit to determine 
# popular parts of a video. this one just counts all views, without regard to user
@login_required
def display_interval_views(request, ta_id):
    user = AnonymousUser()
    if request.user.is_authenticated():
        user = request.user
    id=int(ta_id)
    ta = TopicAssignment.objects.get(pk=id)

    img_url = get_img_url(ta_id)
    print "img_url = " + img_url
    context = {
        "ta_start" : ta.start_time,
        "ta_id":ta_id,
        "user":user,
        "ta_stop" : ta.stop_time,
        "selected_ta" : ta,
        "img_url" : img_url
        }
    template = "display_interval_views.html"
    return render_to_response(template, context)


