

from django.db import models
from django.conf import settings
import datetime


QUIZ_CHOICES = (
    (1, 'Quiz 1'),
    (2, 'Quiz 2'),
    (3, 'Quiz 3'),
    (4, 'Quiz 4'),
    (5, 'Quiz 5'),
    )

STAFF_CHOICES = (
    ('LA', 'Undergraduate Lab Assistant'),
    ('TA', 'Graduate Teaching Assistant'),
    ('Head TA', 'Head Teaching Assistant'),
    ('Lecturer', 'Lecturer'),
    ('Admin', 'Administrative Assistant'),
    )

SEMESTER_CHOICES = (
    ('S11', 'Spring 2011'),
    ('F10', 'Fall 2010'),
    ('S10', 'Spring 2010'),
    ('F09', 'Fall 2009'),
    ('S09', 'Spring 2009'),
    ('F08', 'Fall 2008'),
    ('S08', 'Spring 2008'),
    ('F07', 'Fall 2007'),
    ('S07', 'Spring 2007'),
    ('F06', 'Fall 2006'),
    ('S06', 'Spring 2006'),
    ('F05', 'Fall 2005'),
    )

LAB_CHOICES = (
    (1, 'Lab 1'),
    (2, 'Lab 2'),
    (3, 'Lab 3'),
    (4, 'Lab 4'),
    (5, 'Lab 5'),
    (6, 'Lab 6'),
    (7, 'Lab 7'),
    (8, 'Lab 8'),
    (9, 'Design Project'),
    )



class Student(models.Model):
    athena_id = models.CharField(max_length=8, primary_key=True)
    student_id = models.IntegerField(max_length=9, unique=True)
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    class_year = models.IntegerField(max_length=4)

    def what_fields(self):
        return "athena_id (CharField), student_id (IntegerField), last_name (CharField), first_name (CharField), class_year (IntegerField)"

    def __unicode__(self):
        return self.athena_id


class StaffMember(models.Model):
    athena_id = models.CharField(max_length=8, primary_key=True)
    email = models.EmailField(max_length=20)
    type = models.CharField(max_length=8, choices=STAFF_CHOICES)
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
 

    def __unicode__(self):
        return self.athena_id



class Quiz(models.Model):
    num = models.IntegerField(max_length=1, choices=QUIZ_CHOICES)
    #quiz_date = models.DateField(auto_now=False, auto_now_add=False)
    semester = models.CharField(max_length=3, choices=SEMESTER_CHOICES)

    def natural_key(self):
        return (self.semester, self.num)

    def __unicode__(self):
        return u'%i %s' % (self.num, self.semester)

    class Meta:
        unique_together = (('semester', 'num'))
        ordering=['num']


class Lab(models.Model):
    num = models.IntegerField(choices=LAB_CHOICES)
    submit_due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    checkoff_due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    semester= models.CharField(max_length=3, choices=SEMESTER_CHOICES)
    max_score = models.FloatField()
    
    def natural_key(self):
        return (self.num, self.semester)

    def __unicode__(self):
        return u'%s (%s)' % (self.num, self.semester)

    class Meta:
        unique_together = (('num', 'semester'))
        ordering=['num']
