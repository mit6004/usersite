

from django.db import models
from django.conf import settings
import datetime, os
from usersite.tutorials.models import *

   
class QuizGrade(models.Model):
    quiz = models.ForeignKey(Quiz)
    ## haven't said "is_staff=False" here because maybe 
    ## staff members would want to save Quiz records for draft editing
    student = models.ForeignKey(User)
    score = models.FloatField()

    def natural_key(self):
        return (self.student, self.quiz)

    class Meta:
        unique_together = (('student', 'quiz'))

    def __unicode__(self):
        return u'%s %s %d' % (self.student, self.quiz, self.score)

    

class LabRecord(models.Model):
    ## similarly, haven't said is_staff=False because staff 
    ## members can have a submission record, too.
    student = models.ForeignKey(User)
    lab = models.ForeignKey(Lab)
    # PYthon property also in end note notes.
    checkoff_completed = models.BooleanField(default=True)
    online_questions = models.BooleanField(default=True)
    semester = models.CharField(max_length=3, choices=SEMESTER_CHOICES)
    
    def natural_key(self):
        return (self.student, self.lab)

    class Meta:
        unique_together = (('student', 'lab'))

    def __unicode__(self):
        return u'%s\'s %s' % (self.student, self.lab)

    def get_late_multiplier(self):
        submit_set=self.labsubmission_set.filter(passed=True)
        checkoff_set=self.checkoffmeeting_set.filter(passed=True)
        submit_multiplier=0.5
        checkoff_multiplier=0.5
        for submit in submit_set:
            if (submit.time < self.lab.submit_due_date):
                print "submission for lab %s on time for %s" % (self.lab.num, self.student.get_profile().athena_id)
                submit_multiplier=1
        for checkoff in checkoff_set:
            if (checkoff.time < self.lab.checkoff_due_date):
                print "checkoff for lab %s on time for %s" % (self.lab.num, self.student.get_profile().athena_id)
                checkoff_multiplier=1
        if ( ( checkoff_set.count()==0 ) or ( submit_set.count()==0 ) ):
            # Then the student had NO submissions!
            print "no submissions for %s" % (self.student.get_profile().athena_id)
            return 0
        else:
            return submit_multiplier*checkoff_multiplier

    def _get_score(self):
        return self.lab.max_score*self.get_late_multiplier()
    score = property(_get_score)

    def _get_upload_stem(self):
        return '%s/%s/%s/' %(self.lab.semester, 
                             self.student.get_profile().athena_id, 
                             self.lab.num)            
    upload_stem = property(_get_upload_stem)

    def _get_help_records(self):
        return self.helpmeeting_set.all()
    help_records = property(_get_help_records)


class LabEvent(MediaSubmission):
    # points to a particular student/lab grade entry
    record = models.ForeignKey(LabRecord)

    def natural_key(self):
        return (self.record, self.time)

    class Meta:
        unique_together = (('record', 'time'))
        get_latest_by='time'
        abstract=True
 
    def __unicode__(self):
        return u'%s' %(self.time)

    def _get_event_type(self):
        return self.__class__.__name__
    event_type=property(_get_event_type)

    def _get_upload_location(self):
        return 'Misc/%s/%s' %(self.semester, self.type)
    upload_location = property(_get_upload_location)
    file = models.FileField(upload_to=upload_location, null=True, blank=True)

    def _get_public_location(self):
        return os.path.join(self.upload_location, self.file.name)
    public_location=property(_get_public_location)

    def save(self):
        if self.file:
            write_uploaded_file(self.file, self.upload_location)
            self.file_name=self.file.name
            print "writing %s upload_location: %s" %(self.file_name, self.upload_location)
            super(LabEvent, self).save()

class CheckoffMeeting(LabEvent):
    passed = models.BooleanField()
    staff_member = models.ForeignKey(User)
    ## limit so that a staff member has to be involved

    def on_time(self):
        return self.time<self.record.lab.checkoff_due_date


class HelpMeeting(LabEvent):
    ## limit so only staff can check off
    staff_member = models.ForeignKey(User)


class LabSubmission(LabEvent):
    passed = models.BooleanField()

    def on_time(self):
        return self.time<self.record.lab.submit_due_date
       
 

        
