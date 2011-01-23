
## testing jquery ##
## server side handler function 
def post_handler(request):
    iform_start = request.POST['iform_start']
    print "iform_start : %s \n" %(iform_start)
    iform_end = request.POST['iform_end']
    print "iform_end : %s \n" %(iform_end)
    return HttpResponse("{'response_text: recieved.'}", 
                                   mimetype="application/json")

    
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
