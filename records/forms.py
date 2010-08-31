from django.shortcuts import render_to_response
from records.models import *
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django import forms

class StudentForm(ModelForm):
    ## Keeping name of "student" even if we are using
    ## the django User model form the admin app
    fields=['username','first_name','last_name']
    class Meta:
        model=User
        

def add_student(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            for lab in Lab.objects.all():
                record = LabRecord(student=student, lab=lab)
                record.save()
            student.save()

            return HttpResponseRedirect('/students/')
    else:
        form = StudentForm()

    return render_to_response('new_student_form.html', 
                              { 'student_form': form, })

#class DelStudentForm(forms.Form):
#    athena_id = forms.CharField(max_length=8)


class CheckoffMeetingForm(ModelForm):
    file=forms.FileField()
    
    class Meta:
        model=CheckoffMeeting
        fields=['passed', 'comments', 'staff_member', 'file']

class HelpMeetingForm(ModelForm):
    file=forms.FileField()

    class Meta:
        model=HelpMeeting
        fields=['comments', 'staff_member', 'file']




#class VideoFileForm(ModelForm):
#    file=forms.FileField()#

#    class Meta:
#        model=VideoFile
#        fields=['file']
