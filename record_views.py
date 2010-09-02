from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from records.models import *
from tutorials.models import *
import student_views
from django.template import RequestContext
from django.conf import settings
from records.forms import StudentForm, CheckoffMeetingForm, HelpMeetingForm
from django.contrib.auth.decorators import login_required
import datetime, os


lab_num2name={
    1:'Lab 1',
    2:'Lab 3',
    3:'Lab 3',
    4:'Lab 4',
    5:'Lab 5',
    6:'Lab 6',
    7:'Lab 7',
    8:'Lab 8',
    9:'Design Project'}



def student_list(request):
    #student_list = Student.objects.all()
    ## change to just give a list of all non-staff users.
    ## maybe add semester support later, but use "is_active=True" for now
    student_list = User.objects.filter(is_staff=False, is_active=True)
    student_list_template = 'student_list.html'

    if request.method =='POST':
        add_form = StudentForm(request.POST)
        if add_form.is_valid():
            student = add_form.save(commit=False)
            for lab in Lab.objects.all():
                record = LabRecord(student=student, lab=lab)
                record.save()
            student.save()

            return HttpResponseRedirect('/students/')
    else:
        add_form = StudentForm()

    student_list_dict = {
        'student_list': student_list,
        'add_form': add_form}
    return render_to_response(student_list_template, student_list_dict)


def student_detail(request, athena_id):
#    student = Student.objects.get(pk=athena_id)
    # don't need active or staff specifiers
    # but rather, we want the User object associated with the 
    ## profile that has that primary key
    profile = UserProfile.objects.get(pk=athena_id)
    student = profile.user
    record_list = student.labrecord_set.all()
    template_name='student_detail.html'
    return render_to_response(template_name, {'student': student, 'record_list': record_list})


@login_required
def student_record(request):
    student_dict=student_views.get_student_info(request)
    record_list=student_dict['student'].labrecord_set.all()
    template='student_detail.html'
    return render_to_response(template, {'record_list' : record_list,}, 
                              context_instance=
                              RequestContext(request, 
                                             processors=[student_views.get_student_info]))



def checkoff_records(request, athena_id, lab_number):
    # Remember that lab_number is coming in as a unicde representation of the int
    lab_number=int(lab_number)
    # same as above
    student = UserProfile.objects.get(pk=athena_id).user

    record = student.labrecord_set.filter(lab__num__exact=lab_number).get()
    lab_name = lab_num2name[lab_number]
    checkoff_list = record.checkoffmeeting_set.all()
    checkoff_dict = {
        'student':student,
        'lab_name':lab_name,
        'meeting_list':checkoff_list,
        'passed_field':True,
        }
    checkoff_template = 'meeting_records.html'
    return render_to_response(checkoff_template, checkoff_dict)



def help_records(request, athena_id, lab_number):
    # Remember that lab_number is coming in as a unicde representation of the int
    lab_number=int(lab_number)
    ## Same modification to student field
    student = UserProfile.objects.get(pk=athena_id).user

    record = student.labrecord_set.filter(lab__num__exact=lab_number).get()
    lab_name = lab_num2name[lab_number]
    help_list = record.helpmeeting_set.all()
    help_dict = {
        'student':student,
        'lab_name':lab_name,
        'meeting_list':help_list,
        'passed_field':False}
    help_template = 'meeting_records.html'
    return render_to_response(help_template, help_dict)


def add_checkoff(request, athena_id, lab_number):
    return add_meeting(request, athena_id, lab_number, True)

def add_help(request, athena_id, lab_number):
    return add_meeting(request, athena_id, lab_number, False)

def add_meeting(request, athena_id, lab_number, is_checkoff):
    # Remember that lab_number is coming in as a unicde representation of the int
    lab_number=int(lab_number)
    ## standatd student modification
    student = UserProfile.objects.get(pk=athena_id).user
    record = student.labrecord_set.filter(lab__num__exact=lab_number).get()
    lab_name = lab_num2name[lab_number]
    time = datetime.datetime.now()
    print "(add_meeting) adding meeting for student %s %s and lab %s" %(student.first_name, student.last_name, lab_name)

    if request.method=="POST":
        print "(add_meeting) request.method == POST is true"
        if is_checkoff:
            meeting_form = CheckoffMeetingForm(request.POST, request.FILES)
        else:
            meeting_form = HelpMeetingForm(request.POST, request.FILES)

        
        if meeting_form.is_valid():
            print "(add_meeting) meeting_form is valid"

            meeting = meeting_form.save(commit=False)
            meeting.time=datetime.datetime.now()
            meeting.student=student
            meeting.record=record
            file = request.FILES['file']
            meeting.file=file
            print "meeting.file.name = %s" %(meeting.file.name)
            print "(add_meeting) file name is %s" %(file.name)
#            meeting.file_name=file.name
            # custom save method writes bound file
            meeting.save()
            return HttpResponseRedirect('/students/%s/' %(athena_id) )
    else:
        if is_checkoff: meeting_form = CheckoffMeetingForm()
        else: meeting_form = HelpMeetingForm()

    meeting_dict = { 
        'record':record,'time':time,'is_checkoff':is_checkoff,'meeting_form':meeting_form,}
    template = 'add_meeting.html'
    return render_to_response(template, meeting_dict)



#def get_public_location(file, upload_location):
#    public_location = os.path.join(upload_location, file.name)
#    print "(get_public_location) public_location is %s \n" %(public_location)
#    return public_location
    


def play_video(request, video_id):
    video_id = int(video_id)
    video = VideoFile.objects.get(pk=video_id)
    template = 'popup_video.html'
    dict = {'video': video,}

    print "public path for video is %s" %(video.file_path)

    return render_to_response(template, dict)
