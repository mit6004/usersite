from django.db import models
from usersite.records.models import *
from usersite.tutorials.models import *

import datetime

def make():


    ## Student ##


    ## changed to swiotch Students and StaffMembers to Users... Should have everything else 
    ## tied to "User" instances that are usually called 'student' as the variable

    #benbit=Student(athena_id="benbit", student_id="900000001", last_name="Bitdiddle", first_name="Ben", class_year="2011")
    #aphacker=Student(athena_id="aphacker", student_id="900000002", last_name="Hacker", first_name="Alyssa", class_year="2011")
    #chipahoy=Student(athena_id="chipahoy", student_id="900000003", last_name="Ahoy", first_name="Chip", class_year="2011")
    #alogue=Student(athena_id="alogue", student_id="900000004", last_name="Logue", first_name="Anna", class_year="2011")

    def make_student(athena_id, first_name, last_name, student_id):
        student=User.objects.filter(username=athena_id)
        if not student.count():
            s=User.objects.create_user(athena_id, '%s@mit.edu' %(athena_id), student_id)
            s.first_name=first_name
            s.last_name=last_name
            s.is_staff=False
            p = s.get_profile()
            p.student_id=student_id
            s.save()
            p.save()
            return s

        else:
            s = student.get(username=athena_id)
            s.first_name=first_name
            s.last_name=last_name
            s.is_staff=False
            s.save()
            return s 

    benbit=make_student('benbit', 'Ben', 'Bitdiddle', '900000001')
    aphacker=make_student('aphacker', 'Alyssa P.', 'Hacker', '900000002') 
    chipahoy=make_student('chipahoy', 'Chip', 'Ahoy', '900000003')
    alogue=make_student('alogue', 'Anna', 'Logue', '900000004')

    
    ## LABS ##

    S10_L1 = Lab(num=1, submit_due_date=datetime.datetime(2010, 2, 19, 6), semester="S10",
                 checkoff_due_date=datetime.datetime(2010, 2, 25, 23, 59, 59), max_score=3)

    S10_L2 = Lab(num=2, submit_due_date=datetime.datetime(2010, 2, 25, 6), semester="S10",
                 checkoff_due_date=datetime.datetime(2010, 3, 4, 23, 59, 59), max_score=5)

    S10_L3 = Lab(num=3, submit_due_date=datetime.datetime(2010, 3, 4, 6), semester="S10",
                 checkoff_due_date=datetime.datetime(2010, 3, 11, 23, 59, 59), max_score=10)

    S10_L4 = Lab(num=4, submit_due_date=datetime.datetime(2010, 3, 18, 6), semester="S10",
                 checkoff_due_date=datetime.datetime(2010, 4, 1, 23, 59, 59), max_score=4)

    S10_L5 = Lab(num=5, submit_due_date=datetime.datetime(2010, 4, 1, 6), semester="S10",
                 checkoff_due_date=datetime.datetime(2010, 4, 8, 23, 59, 59), max_score=6)

    S10_L6 = Lab(num=6, submit_due_date=datetime.datetime(2010, 4, 15, 6), semester="S10",
                 checkoff_due_date=datetime.datetime(2010, 4, 22, 23, 59, 59), max_score=25)

    S10_L7 = Lab(num=7, submit_due_date=datetime.datetime(2010, 4, 29, 6), semester="S10",
                 checkoff_due_date=datetime.datetime(2010, 5, 6, 23, 59, 59), max_score=7)

    S10_L8 = Lab(num=8, submit_due_date=datetime.datetime(2010, 5, 6, 6), semester="S10",
                 checkoff_due_date=datetime.datetime(2010, 5, 6, 23, 59, 59), max_score=15)

    S10_DP = Lab(num=9, submit_due_date=datetime.datetime(2010, 5, 12, 6), semester="S10",
                 checkoff_due_date=datetime.datetime(2010, 5, 6, 23, 59, 59), max_score=10)
    S10_L1.save()
    S10_L2.save()
    S10_L3.save()
    S10_L4.save()
    S10_L5.save()
    S10_L6.save()
    S10_L7.save()
    S10_L8.save()
    S10_DP.save()



    ## LabRecord ##

    aphacker_L1 =LabRecord(score=3)
    aphacker_L2 =LabRecord(score=5)
    aphacker_L3 =LabRecord(score=10)
    aphacker_L4 =LabRecord(score=4)
    aphacker_L5 =LabRecord(score=6)
    aphacker_L6 =LabRecord(score=25)
    aphacker_L7 =LabRecord(score=7)
    aphacker_L8 =LabRecord(score=15)
    aphacker_DP =LabRecord(score=10)

    aphacker_L1.lab=S10_L1
    aphacker_L2.lab=S10_L2
    aphacker_L3.lab=S10_L3
    aphacker_L4.lab=S10_L4
    aphacker_L5.lab=S10_L5
    aphacker_L6.lab=S10_L6
    aphacker_L7.lab=S10_L7
    aphacker_L8.lab=S10_L8
    aphacker_DP.lab=S10_DP

    aphacker_L1.student=aphacker
    aphacker_L2.student=aphacker
    aphacker_L3.student=aphacker
    aphacker_L4.student=aphacker
    aphacker_L5.student=aphacker
    aphacker_L6.student=aphacker
    aphacker_L7.student=aphacker
    aphacker_L8.student=aphacker
    aphacker_DP.student=aphacker

    aphacker_L1.save()
    aphacker_L2.save()
    aphacker_L3.save()
    aphacker_L4.save()
    aphacker_L5.save()
    aphacker_L6.save()
    aphacker_L7.save()
    aphacker_L8.save()
    aphacker_DP.save()
    

    alogue_L1 =LabRecord(score=3)
    alogue_L2 =LabRecord(score=5)
    alogue_L3 =LabRecord(score=6)
    alogue_L4 =LabRecord(score=4)
    alogue_L5 =LabRecord(score=6)
    alogue_L6 =LabRecord(score=25)
    alogue_L7 =LabRecord(score=7)
    alogue_L8 =LabRecord(score=15)
    alogue_DP =LabRecord(score=3)

    alogue_L1.lab=S10_L1
    alogue_L2.lab=S10_L2
    alogue_L3.lab=S10_L3
    alogue_L4.lab=S10_L4
    alogue_L5.lab=S10_L5
    alogue_L6.lab=S10_L6
    alogue_L7.lab=S10_L7
    alogue_L8.lab=S10_L8
    alogue_DP.lab=S10_DP

    alogue_L1.student=alogue
    alogue_L2.student=alogue
    alogue_L3.student=alogue
    alogue_L4.student=alogue
    alogue_L5.student=alogue
    alogue_L6.student=alogue
    alogue_L7.student=alogue
    alogue_L8.student=alogue
    alogue_DP.student=alogue

    alogue_L1.save()
    alogue_L2.save()
    alogue_L3.save()
    alogue_L4.save()
    alogue_L5.save()
    alogue_L6.save()
    alogue_L7.save()
    alogue_L8.save()
    alogue_DP.save()


    benbit_L1 =LabRecord(score=3)
    benbit_L2 =LabRecord(score=5)
    benbit_L3 =LabRecord(score=6)
    benbit_L4 =LabRecord(score=3)
    benbit_L5 =LabRecord(score=6)
    benbit_L6 =LabRecord(score=20)
    benbit_L7 =LabRecord(score=7)
    benbit_L8 =LabRecord(score=15)
    benbit_DP =LabRecord(score=1)

    benbit_L1.lab=S10_L1
    benbit_L2.lab=S10_L2
    benbit_L3.lab=S10_L3
    benbit_L4.lab=S10_L4
    benbit_L5.lab=S10_L5
    benbit_L6.lab=S10_L6
    benbit_L7.lab=S10_L7
    benbit_L8.lab=S10_L8
    benbit_DP.lab=S10_DP

    benbit_L1.student=benbit
    benbit_L2.student=benbit
    benbit_L3.student=benbit
    benbit_L4.student=benbit
    benbit_L5.student=benbit
    benbit_L6.student=benbit
    benbit_L7.student=benbit
    benbit_L8.student=benbit
    benbit_DP.student=benbit

    benbit_L1.save()
    benbit_L2.save()
    benbit_L3.save()
    benbit_L4.save()
    benbit_L5.save()
    benbit_L6.save()
    benbit_L7.save()
    benbit_L8.save()
    benbit_DP.save()

    chipahoy_L1 =LabRecord(score=3)
    chipahoy_L2 =LabRecord(score=5)
    chipahoy_L3 =LabRecord(score=5)
    chipahoy_L4 =LabRecord(score=3)
    chipahoy_L5 =LabRecord(score=6)
    chipahoy_L6 =LabRecord(score=20)
    chipahoy_L7 =LabRecord(score=7)
    chipahoy_L8 =LabRecord(score=15)
    chipahoy_DP =LabRecord(score=0)

    chipahoy_L1.lab=S10_L1
    chipahoy_L2.lab=S10_L2
    chipahoy_L3.lab=S10_L3
    chipahoy_L4.lab=S10_L4
    chipahoy_L5.lab=S10_L5
    chipahoy_L6.lab=S10_L6
    chipahoy_L7.lab=S10_L7
    chipahoy_L8.lab=S10_L8
    chipahoy_DP.lab=S10_DP

    chipahoy_L1.student=chipahoy
    chipahoy_L2.student=chipahoy
    chipahoy_L3.student=chipahoy
    chipahoy_L4.student=chipahoy
    chipahoy_L5.student=chipahoy
    chipahoy_L6.student=chipahoy
    chipahoy_L7.student=chipahoy
    chipahoy_L8.student=chipahoy
    chipahoy_DP.student=chipahoy

    chipahoy_L1.save()
    chipahoy_L2.save()
    chipahoy_L3.save()
    chipahoy_L4.save()
    chipahoy_L5.save()
    chipahoy_L6.save()
    chipahoy_L7.save()
    chipahoy_L8.save()
    chipahoy_DP.save()


    ## QUIZZES ##

    S10_Q1 = Quiz(num=1, semester="S10")
    S10_Q1.save()
    S10_Q2 = Quiz(num=2, semester="S10")
    S10_Q2.save()
    S10_Q3 = Quiz(num=3, semester="S10")
    S10_Q3.save()
    S10_Q4 = Quiz(num=4, semester="S10")
    S10_Q4.save()
    S10_Q5 = Quiz(num=5, semester="S10")
    S10_Q5.save()



    ## Quiz Grades ##

    benbit_Q1 = QuizGrade(score=18)
    benbit_Q2 = QuizGrade(score=19)
    benbit_Q3 = QuizGrade(score=15)
    benbit_Q4 = QuizGrade(score=18)
    benbit_Q5 = QuizGrade(score=20)

    benbit_Q1.quiz=S10_Q1
    benbit_Q2.quiz=S10_Q2
    benbit_Q3.quiz=S10_Q3
    benbit_Q4.quiz=S10_Q4
    benbit_Q5.quiz=S10_Q5
    
    benbit_Q1.student=benbit
    benbit_Q2.student=benbit
    benbit_Q3.student=benbit
    benbit_Q4.student=benbit
    benbit_Q5.student=benbit

    benbit_Q1.save()
    benbit_Q2.save()
    benbit_Q3.save()
    benbit_Q4.save()
    benbit_Q5.save()


    chipahoy_Q1 = QuizGrade(score=16)
    chipahoy_Q2 = QuizGrade(score=15)
    chipahoy_Q3 = QuizGrade(score=11)
    chipahoy_Q4 = QuizGrade(score=15)
    chipahoy_Q5 = QuizGrade(score=18)
    
    chipahoy_Q1.quiz=S10_Q1
    chipahoy_Q2.quiz=S10_Q2
    chipahoy_Q3.quiz=S10_Q3
    chipahoy_Q4.quiz=S10_Q4
    chipahoy_Q5.quiz=S10_Q5

    chipahoy_Q1.student=chipahoy
    chipahoy_Q2.student=chipahoy
    chipahoy_Q3.student=chipahoy
    chipahoy_Q4.student=chipahoy
    chipahoy_Q5.student=chipahoy

    chipahoy_Q1.save()
    chipahoy_Q2.save()
    chipahoy_Q3.save()
    chipahoy_Q4.save()
    chipahoy_Q5.save()


    alogue_Q1 = QuizGrade(score=21)
    alogue_Q2 = QuizGrade(score=22)
    alogue_Q3 = QuizGrade(score=19)
    alogue_Q4 = QuizGrade(score=21)
    alogue_Q5 = QuizGrade(score=22)

    alogue_Q1.quiz=S10_Q1
    alogue_Q2.quiz=S10_Q2
    alogue_Q3.quiz=S10_Q3
    alogue_Q4.quiz=S10_Q4
    alogue_Q5.quiz=S10_Q5

    alogue_Q1.student=alogue
    alogue_Q2.student=alogue
    alogue_Q3.student=alogue
    alogue_Q4.student=alogue
    alogue_Q5.student=alogue

    alogue_Q1.save()
    alogue_Q2.save()
    alogue_Q3.save()
    alogue_Q4.save()
    alogue_Q5.save()


    aphacker_Q1 = QuizGrade(score=25)
    aphacker_Q2 = QuizGrade(score=24)
    aphacker_Q3 = QuizGrade(score=23)
    aphacker_Q4 = QuizGrade(score=25)
    aphacker_Q5 = QuizGrade(score=24)

    aphacker_Q1.quiz=S10_Q1
    aphacker_Q2.quiz=S10_Q2
    aphacker_Q3.quiz=S10_Q3
    aphacker_Q4.quiz=S10_Q4
    aphacker_Q5.quiz=S10_Q5

    aphacker_Q1.student=aphacker
    aphacker_Q2.student=aphacker
    aphacker_Q3.student=aphacker
    aphacker_Q4.student=aphacker
    aphacker_Q5.student=aphacker

    aphacker_Q1.save()
    aphacker_Q2.save()
    aphacker_Q3.save()
    aphacker_Q4.save()
    aphacker_Q5.save()


    ## StaffMember ##

    ## utility function!

 #   caitlinj=StaffMember(athena_id="caitlinj", email="caitlinj@mit.edu", type="Head TA", last_name="Johnson", first_name="Caitlin")
 #   ward=StaffMember(athena_id="ward", email="ward@mit.edu", type="Lecturer", last_name="Ward", first_name="Steve")
 #   sneuman=StaffMember(athena_id="sneuman", email="sneuman@mit.edu", type="TA", last_name="Neuman", first_name="Sabrina")
 #   sarina=StaffMember(athena_id="sarina", email="sarina@mit.edu", type="LA", last_name="Canelake", first_name="Sarina")
 #   kelleyk=StaffMember(athena_id="kelleyk", email="kelleyk@mit.edu", type="TA", last_name="Kelley", first_name="Kevin")
 #   dcrowell=StaffMember(athena_id="dcrowell", email="dcrowell@mit.edu", type="LA", last_name="Crowell", first_name="David")
  
    def make_staff(athena_id, first_name, last_name):
        staff=User.objects.filter(username=athena_id)
        if not staff.count():
            member=User.objects.create_user(athena_id, '%s@mit.edu' %(athena_id), first_name)
            member.first_name=first_name
            member.last_name=last_name
            member.is_staff=True
            member.save()
            return member
        else:
            member=staff.get()
            member.save()
            return member
        
    caitlinj=make_staff('caitlinj', 'Caitlin', 'Johnson')
    ward=make_staff('ward', 'Steve', 'Ward')
    sneuman=make_staff('sneuman', 'Sabrina', 'Neuman')
    sarina=make_staff('sarina', 'Sarina', 'Canelake')
    kelleyk=make_staff('kelleyk', 'Kevin', 'Kelley')
    dcrowell=make_staff('dcrowell', 'David', 'Crowell')

    ## LabSubmission ##

    aphacker_ls1a=LabSubmission(passed=True, time=datetime.datetime(2010, 2, 11, 17, 14, 32))
    aphacker_ls2a=LabSubmission(passed=True, time=datetime.datetime(2010, 2, 18, 14, 11, 41))
    aphacker_ls3a=LabSubmission(passed=True, time=datetime.datetime(2010, 2, 25, 18, 51, 17))
    aphacker_ls4a=LabSubmission(passed=True, time=datetime.datetime(2010, 3, 11, 16, 41, 51))
    aphacker_ls5a=LabSubmission(passed=True, time=datetime.datetime(2010, 3, 25, 19, 0, 33))
    aphacker_ls6a=LabSubmission(passed=True, time=datetime.datetime(2010, 4, 14, 15, 13, 10))
    aphacker_ls7a=LabSubmission(passed=True, time=datetime.datetime(2010, 4, 29, 13, 41, 22))
    aphacker_ls8a=LabSubmission(passed=True, time=datetime.datetime(2010, 4, 30, 17, 55, 41))
    aphacker_lsdpa=LabSubmission(passed=True, time=datetime.datetime(2010, 5, 6, 10, 1, 36))

    aphacker_ls1a.record=aphacker_L1
    aphacker_ls2a.record=aphacker_L2
    aphacker_ls3a.record=aphacker_L3
    aphacker_ls4a.record=aphacker_L4
    aphacker_ls5a.record=aphacker_L5
    aphacker_ls6a.record=aphacker_L6
    aphacker_ls7a.record=aphacker_L7
    aphacker_ls8a.record=aphacker_L8
    aphacker_lsdpa.record=aphacker_DP

    aphacker_ls1a.save()
    aphacker_ls2a.save()
    aphacker_ls3a.save()
    aphacker_ls4a.save()
    aphacker_ls5a.save()
    aphacker_ls6a.save()
    aphacker_ls7a.save()
    aphacker_ls8a.save()
    aphacker_lsdpa.save()


    alogue_ls1a=LabSubmission(passed=True, time=datetime.datetime(2010, 2, 16, 16, 30, 12))
    alogue_ls2a=LabSubmission(passed=True, time=datetime.datetime(2010, 2, 23, 14, 31, 31))
    alogue_ls3a=LabSubmission(passed=True, time=datetime.datetime(2010, 3, 1, 16, 41, 21))
    alogue_ls4a=LabSubmission(passed=True, time=datetime.datetime(2010, 3, 16, 19, 44, 30))
    alogue_ls5a=LabSubmission(passed=True, time=datetime.datetime(2010, 3, 30, 13, 0, 29))
    alogue_ls6a=LabSubmission(passed=True, time=datetime.datetime(2010, 4, 14, 21, 10, 14))
    alogue_ls7a=LabSubmission(passed=True, time=datetime.datetime(2010, 4, 27, 13, 36, 1))
    alogue_ls8a=LabSubmission(passed=True, time=datetime.datetime(2010, 5, 5, 12, 21, 31))

    alogue_ls1a.record=alogue_L1
    alogue_ls2a.record=alogue_L2
    alogue_ls3a.record=alogue_L3
    alogue_ls4a.record=alogue_L4
    alogue_ls5a.record=alogue_L5
    alogue_ls6a.record=alogue_L6
    alogue_ls7a.record=alogue_L7
    alogue_ls8a.record=alogue_L8

    alogue_ls1a.save()
    alogue_ls2a.save()
    alogue_ls3a.save()
    alogue_ls4a.save()
    alogue_ls5a.save()
    alogue_ls6a.save()
    alogue_ls7a.save()
    alogue_ls8a.save()


    benbit_ls1a=LabSubmission(passed=True, time=datetime.datetime(2010, 2, 17, 14, 39, 32))
    benbit_ls2a=LabSubmission(passed=True, time=datetime.datetime(2010, 2, 23, 17, 26, 41))
    benbit_ls3a=LabSubmission(passed=True, time=datetime.datetime(2010, 3, 3, 18, 51, 53))
    benbit_ls4a=LabSubmission(passed=True, time=datetime.datetime(2010, 3, 17, 20, 10, 42))
    benbit_ls5a=LabSubmission(passed=True, time=datetime.datetime(2010, 4, 1, 12, 10, 51))
    benbit_ls6a=LabSubmission(passed=True, time=datetime.datetime(2010, 4, 15, 14, 51, 21))
    benbit_ls7a=LabSubmission(passed=True, time=datetime.datetime(2010, 4, 28, 17, 21, 10))
    benbit_ls8a=LabSubmission(passed=True, time=datetime.datetime(2010, 5, 5, 14, 13, 6))

    benbit_ls1a.record=benbit_L1
    benbit_ls2a.record=benbit_L2
    benbit_ls3a.record=benbit_L3
    benbit_ls4a.record=benbit_L4
    benbit_ls5a.record=benbit_L5
    benbit_ls6a.record=benbit_L6
    benbit_ls7a.record=benbit_L7
    benbit_ls8a.record=benbit_L8

    benbit_ls1a.save()
    benbit_ls2a.save()
    benbit_ls3a.save()
    benbit_ls4a.save()
    benbit_ls5a.save()
    benbit_ls6a.save()
    benbit_ls7a.save()
    benbit_ls8a.save()


    chipahoy_ls1a=LabSubmission(passed=True, time=datetime.datetime(2010, 2, 18, 15, 59, 41))
    chipahoy_ls2a=LabSubmission(passed=True, time=datetime.datetime(2010, 2, 25, 19, 5, 23))
    chipahoy_ls3a=LabSubmission(passed=False, time=datetime.datetime(2010, 3, 11, 10, 3, 41))
    chipahoy_ls3b=LabSubmission(passed=True, time=datetime.datetime(2010, 3, 11, 18, 0, 51))
    chipahoy_ls4a=LabSubmission(passed=True, time=datetime.datetime(2010, 3, 18, 21, 10, 49))
    chipahoy_ls5a=LabSubmission(passed=True, time=datetime.datetime(2010, 3, 30, 22, 50, 18))
    chipahoy_ls6a=LabSubmission(passed=True, time=datetime.datetime(2010, 4, 16, 3, 13, 31))
    chipahoy_ls7a=LabSubmission(passed=True, time=datetime.datetime(2010, 4, 30, 2, 14, 4))
    chipahoy_ls8a=LabSubmission(passed=True, time=datetime.datetime(2010, 5, 5, 18, 10, 50))

    chipahoy_ls1a.record=chipahoy_L1
    chipahoy_ls2a.record=chipahoy_L2
    chipahoy_ls3a.record=chipahoy_L3
    chipahoy_ls3b.record=chipahoy_L3
    chipahoy_ls4a.record=chipahoy_L4
    chipahoy_ls5a.record=chipahoy_L5
    chipahoy_ls6a.record=chipahoy_L6
    chipahoy_ls7a.record=chipahoy_L7
    chipahoy_ls8a.record=chipahoy_L8

    chipahoy_ls1a.save()
    chipahoy_ls2a.save()
    chipahoy_ls3a.save()
    chipahoy_ls3b.save()
    chipahoy_ls4a.save()
    chipahoy_ls5a.save()
    chipahoy_ls6a.save()
    chipahoy_ls7a.save()
    chipahoy_ls8a.save()



    ## Lab Help ##

    alogue_hm1a = HelpMeeting(time=datetime.datetime(2010, 2, 23, 15, 13, 41))
    alogue_hm3a = HelpMeeting(time=datetime.datetime(2010, 3, 2, 16, 3, 45))
    alogue_hm3b = HelpMeeting(time=datetime.datetime(2010, 3, 1, 14, 3, 45))
    alogue_hm5a = HelpMeeting(time=datetime.datetime(2010, 3, 22, 14, 17, 39))
    alogue_hm6a = HelpMeeting(time=datetime.datetime(2010, 4, 18, 14, 21, 10))
    alogue_hm6b = HelpMeeting(time=datetime.datetime(2010, 4, 20, 19, 25, 10))
    alogue_hm8a = HelpMeeting(time=datetime.datetime(2010, 5, 1, 14, 25, 45))

    alogue_hm1a.staff_member=caitlinj
    alogue_hm3a.staff_member=sneuman
    alogue_hm3b.staff_member=sneuman
    alogue_hm5a.staff_member=kelleyk
    alogue_hm6a.staff_member=dcrowell
    alogue_hm6b.staff_member=dcrowell
    alogue_hm8a.staff_member=sarina

    alogue_hm1a.record=alogue_L1
    alogue_hm3a.record=alogue_L3
    alogue_hm3b.record=alogue_L3
    alogue_hm5a.record=alogue_L5
    alogue_hm6a.record=alogue_L6
    alogue_hm6b.record=alogue_L6
    alogue_hm8a.record=alogue_L8

    alogue_hm1a.save()
    alogue_hm3a.save()
    alogue_hm3b.save()
    alogue_hm5a.save()
    alogue_hm6a.save()
    alogue_hm6b.save()
    alogue_hm8a.save()


    benbit_hm1a = HelpMeeting(time=datetime.datetime(2010, 2, 24, 15, 31, 13))
    benbit_hm2a = HelpMeeting(time=datetime.datetime(2010, 3, 4, 18, 11, 45))
    benbit_hm3a = HelpMeeting(time=datetime.datetime(2010, 3, 9, 19, 3, 21))
    benbit_hm4a = HelpMeeting(time=datetime.datetime(2010, 3, 30, 20, 0, 22))
    benbit_hm5a = HelpMeeting(time=datetime.datetime(2010, 4, 2, 22, 17, 51))
    benbit_hm6a = HelpMeeting(time=datetime.datetime(2010, 4, 22, 14, 15, 40))
    benbit_hm7a = HelpMeeting(time=datetime.datetime(2010, 5, 4, 18, 21, 42))
    benbit_hm8a = HelpMeeting(time=datetime.datetime(2010, 5, 6, 14, 41, 31))

    benbit_hm1a.staff_member=caitlinj
    benbit_hm2a.staff_member=dcrowell
    benbit_hm3a.staff_member=sneuman
    benbit_hm4a.staff_member=kelleyk
    benbit_hm5a.staff_member=ward
    benbit_hm6a.staff_member=sarina
    benbit_hm7a.staff_member=caitlinj
    benbit_hm8a.staff_member=ward

    benbit_hm1a.record=benbit_L1
    benbit_hm2a.record=benbit_L2
    benbit_hm3a.record=benbit_L3
    benbit_hm4a.record=benbit_L4
    benbit_hm5a.record=benbit_L5
    benbit_hm6a.record=benbit_L6
    benbit_hm7a.record=benbit_L7
    benbit_hm8a.record=benbit_L8

    benbit_hm1a.save()
    benbit_hm2a.save()
    benbit_hm3a.save()
    benbit_hm4a.save()
    benbit_hm5a.save()
    benbit_hm6a.save()
    benbit_hm7a.save()
    benbit_hm8a.save()


    chipahoy_hm1a = HelpMeeting(time=datetime.datetime(2010, 2, 24, 17, 4, 42))
    chipahoy_hm2a = HelpMeeting(time=datetime.datetime(2010, 2, 26, 21, 39, 15))
    chipahoy_hm3a = HelpMeeting(time=datetime.datetime(2010, 3, 18, 22, 43, 49))
    chipahoy_hm4a = HelpMeeting(time=datetime.datetime(2010, 3, 18, 22, 55, 24))
    chipahoy_hm5a = HelpMeeting(time=datetime.datetime(2010, 4, 7, 22, 37, 3))
    chipahoy_hm6a = HelpMeeting(time=datetime.datetime(2010, 4, 21, 23, 42, 28))
    chipahoy_hm7a = HelpMeeting(time=datetime.datetime(2010, 5, 6, 13, 21, 21))
    chipahoy_hm7b = HelpMeeting(time=datetime.datetime(2010, 5, 6, 15, 25, 31))
    chipahoy_hm8a = HelpMeeting(time=datetime.datetime(2010, 5, 6, 15, 38, 52))

    chipahoy_hm1a.staff_member=caitlinj
    chipahoy_hm2a.staff_member=dcrowell
    chipahoy_hm3a.staff_member=sneuman
    chipahoy_hm4a.staff_member=sneuman
    chipahoy_hm5a.staff_member=dcrowell
    chipahoy_hm6a.staff_member=sarina
    chipahoy_hm7a.staff_member=kelleyk
    chipahoy_hm7b.staff_member=kelleyk
    chipahoy_hm8a.staff_member=kelleyk

    chipahoy_hm1a.record=chipahoy_L1
    chipahoy_hm2a.record=chipahoy_L2
    chipahoy_hm3a.record=chipahoy_L3
    chipahoy_hm4a.record=chipahoy_L4
    chipahoy_hm5a.record=chipahoy_L5
    chipahoy_hm6a.record=chipahoy_L6
    chipahoy_hm7a.record=chipahoy_L7
    chipahoy_hm7b.record=chipahoy_L7
    chipahoy_hm8a.record=chipahoy_L8

    chipahoy_hm1a.save()
    chipahoy_hm2a.save()
    chipahoy_hm3a.save()
    chipahoy_hm4a.save()
    chipahoy_hm5a.save()
    chipahoy_hm6a.save()
    chipahoy_hm7a.save()
    chipahoy_hm7b.save()
    chipahoy_hm8a.save()

    
    ## CheckoffMeeting ##

    aphacker_cm1a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 2, 17, 15, 14, 32))
    aphacker_cm2a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 2, 24, 16, 06, 25))
    aphacker_cm3a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 2, 19, 42, 05))
    aphacker_cm4a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 17, 17, 35, 42))
    aphacker_cm5a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 29, 16, 28, 56))
    aphacker_cm6a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 4, 15, 18, 30, 40))
    aphacker_cm7a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 4, 28, 16, 13, 23))
    aphacker_cm8a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 5, 5, 17, 29, 49))

    aphacker_cm1a.staff_member=ward
    aphacker_cm2a.staff_member=caitlinj
    aphacker_cm3a.staff_member=sneuman
    aphacker_cm4a.staff_member=ward
    aphacker_cm5a.staff_member=sarina
    aphacker_cm6a.staff_member=caitlinj
    aphacker_cm7a.staff_member=dcrowell
    aphacker_cm8a.staff_member=kelleyk

    aphacker_cm1a.record=aphacker_L1
    aphacker_cm2a.record=aphacker_L2
    aphacker_cm3a.record=aphacker_L3
    aphacker_cm4a.record=aphacker_L4
    aphacker_cm5a.record=aphacker_L5
    aphacker_cm6a.record=aphacker_L6
    aphacker_cm7a.record=aphacker_L7
    aphacker_cm8a.record=aphacker_L8
    
    aphacker_cm1a.save()
    aphacker_cm2a.save()
    aphacker_cm3a.save()
    aphacker_cm4a.save()
    aphacker_cm5a.save()
    aphacker_cm6a.save()
    aphacker_cm7a.save()
    aphacker_cm8a.save()


    alogue_cm1a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 2, 23, 16, 13, 41))
    alogue_cm2a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 2, 14, 34, 25))
    alogue_cm3a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 5, 17, 3, 45))
    alogue_cm4a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 18, 20, 4, 28))
    alogue_cm5a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 30, 13, 17, 39))
    alogue_cm6a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 4, 21, 21, 25, 10))
    alogue_cm7a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 5, 4, 18, 56, 4))
    alogue_cm8a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 5, 5, 14, 25, 45))

    alogue_cm1a.staff_member=caitlinj
    alogue_cm2a.staff_member=sarina
    alogue_cm3a.staff_member=sneuman
    alogue_cm4a.staff_member=kelleyk
    alogue_cm5a.staff_member=dcrowell
    alogue_cm6a.staff_member=dcrowell
    alogue_cm7a.staff_member=ward
    alogue_cm8a.staff_member=sarina

    alogue_cm1a.record=alogue_L1
    alogue_cm2a.record=alogue_L2
    alogue_cm3a.record=alogue_L3
    alogue_cm4a.record=alogue_L4
    alogue_cm5a.record=alogue_L5
    alogue_cm6a.record=alogue_L6
    alogue_cm7a.record=alogue_L7
    alogue_cm8a.record=alogue_L8

    alogue_cm1a.save()
    alogue_cm2a.save()
    alogue_cm3a.save()
    alogue_cm4a.save()
    alogue_cm5a.save()
    alogue_cm6a.save()
    alogue_cm7a.save()
    alogue_cm8a.save()


    benbit_cm1a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 2, 24, 15, 31, 13))
    benbit_cm2a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 4, 18, 11, 45))
    benbit_cm3a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 9, 19, 3, 21))
    benbit_cm4a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 30, 20, 0, 22))
    benbit_cm5a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 4, 2, 22, 17, 51))
    benbit_cm6a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 4, 22, 14, 15, 40))
    benbit_cm7a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 5, 4, 18, 21, 42))
    benbit_cm8a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 5, 6, 14, 41, 31))

    benbit_cm1a.staff_member=caitlinj
    benbit_cm2a.staff_member=dcrowell
    benbit_cm3a.staff_member=sneuman
    benbit_cm4a.staff_member=kelleyk
    benbit_cm5a.staff_member=ward
    benbit_cm6a.staff_member=sarina
    benbit_cm7a.staff_member=caitlinj
    benbit_cm8a.staff_member=ward

    benbit_cm1a.record=benbit_L1
    benbit_cm2a.record=benbit_L2
    benbit_cm3a.record=benbit_L3
    benbit_cm4a.record=benbit_L4
    benbit_cm5a.record=benbit_L5
    benbit_cm6a.record=benbit_L6
    benbit_cm7a.record=benbit_L7
    benbit_cm8a.record=benbit_L8

    benbit_cm1a.save()
    benbit_cm2a.save()
    benbit_cm3a.save()
    benbit_cm4a.save()
    benbit_cm5a.save()
    benbit_cm6a.save()
    benbit_cm7a.save()
    benbit_cm8a.save()


    chipahoy_cm1a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 2, 24, 17, 4, 42))
    chipahoy_cm2a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 2, 26, 21, 39, 15))
    chipahoy_cm3a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 18, 22, 43, 49))
    chipahoy_cm4a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 3, 18, 22, 55, 24))
    chipahoy_cm5a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 4, 7, 22, 37, 3))
    chipahoy_cm6a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 4, 21, 23, 42, 28))
    chipahoy_cm7a = CheckoffMeeting(passed=False, time=datetime.datetime(2010, 5, 6, 13, 21, 21))
    chipahoy_cm7b = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 5, 6, 15, 25, 31))
    chipahoy_cm8a = CheckoffMeeting(passed=True, time=datetime.datetime(2010, 5, 6, 15, 38, 52))

    chipahoy_cm1a.staff_member=caitlinj
    chipahoy_cm2a.staff_member=dcrowell
    chipahoy_cm3a.staff_member=sneuman
    chipahoy_cm4a.staff_member=sneuman
    chipahoy_cm5a.staff_member=dcrowell
    chipahoy_cm6a.staff_member=sarina
    chipahoy_cm7a.staff_member=kelleyk
    chipahoy_cm7b.staff_member=kelleyk
    chipahoy_cm8a.staff_member=kelleyk

    chipahoy_cm1a.record=chipahoy_L1
    chipahoy_cm2a.record=chipahoy_L2
    chipahoy_cm3a.record=chipahoy_L3
    chipahoy_cm4a.record=chipahoy_L4
    chipahoy_cm5a.record=chipahoy_L5
    chipahoy_cm6a.record=chipahoy_L6
    chipahoy_cm7a.record=chipahoy_L7
    chipahoy_cm7b.record=chipahoy_L7
    chipahoy_cm8a.record=chipahoy_L8

    chipahoy_cm1a.save()
    chipahoy_cm2a.save()
    chipahoy_cm3a.save()
    chipahoy_cm4a.save()
    chipahoy_cm5a.save()
    chipahoy_cm6a.save()
    chipahoy_cm7a.save()
    chipahoy_cm7b.save()
    chipahoy_cm8a.save()






