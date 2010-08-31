from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from records import models

from django.conf import settings
from forms import StudentForm, VideoFileForm, CheckoffMeetingForm, HelpMeetingForm
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
    student_list = models.Student.objects.all()
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
    student = models.Student.objects.get(pk=athena_id)
    record_list = student.labrecord_set.all()
    template_name='student_detail.html'
    return render_to_response(template_name, {'student': student, 'record_list': record_list})


def checkoff_records(request, athena_id, lab_number):
    # Remember that lab_number is coming in as a unicde representation of the int
    lab_number=int(lab_number)
    student = models.Student.objects.get(pk=athena_id)
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

    student = models.Student.objects.get(pk=athena_id)
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
    student = models.Student.objects.get(pk=athena_id)
    record = student.labrecord_set.filter(lab__num__exact=lab_number).get()
    lab_name = lab_num2name[lab_number]
    time = datetime.datetime.now()
    if request.method=='POST':
        video_form = VideoFileForm(request.POST, request.FILES)
        if is_checkoff:
            meeting_form = CheckoffMeetingForm(request.POST)
        else:
            meeting_form = HelpMeetingForm(request.POST)

        if meeting_form.is_valid() and video_form.is_valid():
            meeting = meeting_form.save(commit=False)
            video = video_form.save(commit=False)
            file = request.FILES['file']
            
            if is_checkoff:
                upload_location = '%s/%s/%s/checkoff' %(record.lab.semester, athena_id, lab_number)            
            else:
                upload_location = '%s/%s/%s/help' %(record.lab.semester, athena_id, lab_number)            
            
            video.public_location = get_public_location(file, upload_location)
            video.filesystem_path = get_filesystem_path(file, upload_location)
            video.file_name = file.name
            #print "(add_help) about to try writing file %s" %(file.name)
            write_uploaded_file(file, video.filesystem_path)
            meeting.time=datetime.datetime.now()
            meeting.student=student
            meeting.record=record
            #print "(add_help) setting video.public_location to %s" %(video.public_location)
            #print "(add_help) setting video.filesystem_path to %s" %(video.filesystem_path)
            video.save()
            meeting.video=video
            meeting.save()
            return HttpResponseRedirect('/students/%s/' %(student.athena_id) )
    else:
        video_form = VideoFileForm()
        if is_checkoff: meeting_form = CheckoffMeetingForm()
        else: meeting_form = HelpMeetingForm()

    meeting_dict = { 
        'student':student,'record':record,'time':time,'is_checkoff':is_checkoff,
        'video_form':video_form,'meeting_form': meeting_form,}
    template = 'add_video_record.html'
    return render_to_response(template, meeting_dict)

def get_filesystem_path(file, upload_location):
    # Makes the directory structure in the MEDIA_ROOT directory if not there already
    filesystem_path = "%s%s" %(settings.MEDIA_ROOT, upload_location)
    print "(get_filesystem_path) filesystem_path is %s\n" %(filesystem_path)
    try:
        os.makedirs(filesystem_path)
        print "(get_filesystem_path) No directory at %s when trying to upload %s\n" %(upload_location, file.name)
    except:
        print "(get_filesystem_path) trying to open the file path for %s\n" %(file.name)
    return filesystem_path


def get_public_location(file, upload_location):
    public_location = os.path.join(upload_location, file.name)
    print "(get_public_location) public_location is %s \n" %(public_location)
    return public_location
    

def write_uploaded_file(file, filesystem_path):
    filesystem_location = os.path.join(filesystem_path, file.name)
    #print "file path complete\n"
    destination = open(filesystem_location, 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    print "I didn't have an error yet and I finished writing the chunks"
    destination.close()


def play_video(request, video_id):
    video_id = int(video_id)
    video = models.VideoFile.objects.get(pk=video_id)
    template = 'popup_video.html'
    dict = {'video': video,}

    print "public path for video is %s" %(video.file_path)

    return render_to_response(template, dict)
