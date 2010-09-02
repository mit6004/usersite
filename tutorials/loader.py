from models import *
from django.db import models
from django.contrib.auth.models import User 
from django.core.files import File
import os, fnmatch, re
from django.conf import settings
from models import PublicVideo







def make():


## ----- Students ----- ##

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


## ----- Staff Members ----- ##


  
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
        
    ward=make_staff('ward', 'Steve', 'Ward')
    cjt=make_staff('cjt', 'Chris', 'Terman')
    
    caitlinj=make_staff('caitlinj', 'Caitlin', 'Johnson')
    sneuman=make_staff('sneuman', 'Sabrina', 'Neuman')
    kelleyk=make_staff('kelleyk', 'Kevin', 'Kelley')

    sarina=make_staff('sarina', 'Sarina', 'Canelake')
    dcrowell=make_staff('dcrowell', 'David', 'Crowell')
    renminbi=make_staff('renminbi', 'Becky', 'Bianco')
    bbasham=make_staff('bbasham', 'Brian', 'Basham')
    colosimo=make_staff('colosimo', 'Joe', 'Colosimo')
    kasittig=make_staff('kasittig', 'Karen', 'Sittig')
    drews=make_staff('drews', 'Andrew', 'Shapiro')

    

## ----- Lecture ----- ##


    staff_list = User.objects.filter(is_staff=True)
    
    semesters=[tuple[0] for tuple in SEMESTER_CHOICES]
    vid_types=[tuple[0] for tuple in VIDEO_CHOICES]
    usernames=[user.username for user in staff_list]
    print "semesters: %s" %(semesters)
    print "usernames: %s" %(usernames)



    def fs_location(auth, type, term):
        return os.path.join(settings.MEDIA_ROOT, auth, type, term)

    def is_video(file_name):
        extension=os.path.splitext(file_name)[1]
        for type in VIDEO_TYPE_LIST:
            if extension==type:
                return True
        return False
        
    def remove_dupes(directory, file):
    #print "(remove_dupes) file: %s" %(file)
        for extension in VIDEO_TYPE_LIST:
            stem = os.path.splitext(os.path.split(file)[1])[0]
            for other_file in os.listdir(directory):
                other_name=os.path.split(other_file)[1]
                [other_stem, other_extension]=os.path.splitext(other_name)[0:2]
                if re.match(stem, other_stem):
                    if other_stem[-1]=='_' and other_extension==extension:
                    #parts=re.split('_+.', other_file)
                        # split around the underscores indicating dupes
                    #if parts[0]==stem and parts[1]==extension:
                        #print "(remove_dupes) removing %s\n" %(other_file)
                        os.remove(os.path.join(directory, other_file))
                        return True    
        
    def already_there(author, type, semester, file):
        authors = PublicVideo.objects.filter(author=author)
        types = authors.filter(type=type)
        semesters = types.filter(semester=semester)
        return semesters.filter(file_name=file).count()

    def load_video(author, type, semester, video_path):        
        video_name=os.path.split(video_path)[1]
        if not already_there(author, type, semester, video_name):
        ## get the user object with this username to assign it
            user_obj = staff_list.get(username=author)
            vid = PublicVideo(author=user_obj, type=type, semester=semester, file_name=video_name)
        #       print "file_path in loader is %s \n" %(video_path)
            fil = File(open(video_path, 'rb'))
            vid.file_name=video_name
        #print "(make_video) vid.file_name=%s  and fil=%s\n" %(vid.file_name, fil)
            vid.file.save(vid.file_name, fil, save=False)
        #print "(make_video) vid.file = %s \n" %(vid.file)
            vid.save()
            return vid

                 

    ## look by staff/type/semester
    def find_media():
        for username in usernames:
#            print "(find_media) --- username: %s\n" %(username)
            for vid_type in vid_types:
#                print "(find_media) ------ vid_type: %s\n" %(vid_type)
                for semester in semesters:
#                    print "(find_media) --------- semester: %s\n" %(semester)
                    directory =fs_location(username, vid_type, semester)
                    ## ONLY CHECK EXISTING DIRECTORIES!! ##
                    if os.path.exists(directory):
#                        print "(find_media) existing directory at: %s\n" %(directory)
                        ## look at each file in the directory to laod 
                        ## after duplicates are removed so we don't 
                        ## laod in duplicate objects with the same file
                        for file in os.listdir(directory):
                        ## and see if it's a movie file
                            if is_video(file):
                                proposed_path = os.path.join(directory, file)
#                                print "(find_media) found media object at %s\n" %(proposed_path)
                                new_vid=load_video(username, vid_type, semester, proposed_path)
#                                print "(find_media) calling remove_dupes in %s for file: %s" %(directory, file)
                                new_vid.save()
                                remove_dupes(directory, file)
                                
                                    ## if we had to remove dupes, then fix the file name
                                new_vid.file_name=file
#                                print "assigning %s to file_name" %(os.path.split(file)[1])
                                new_vid.save()
    print "Finding Media"
    find_media()



## ------ Topics ------ ##

    titles = {
        'L03.mov':'Lecture 3',
        'L04.mov':'Lecture 4',
        'L05.mov':'Lecture 5',
        'L06.mov':'Lecture 6',
        'L07.mov':'Lecture 7',
        'L08.mov':'Lecture 8',
        'L09.mov':'Lecture 9',
        'L10.mov':'Lecture 10',
        'L11.mov':'Lecture 11',
        'L14.mov':'Lecture 14',
        'L15.mov':'Lecture 15',
        'L16.mov':'Lecture 16',
        'L17.mov':'Lecture 17',
        'L18.mov':'Lecture 18',
        'L19.mov':'Lecture 19',
        'L20.mov':'Lecture 20',
        'L21.mov':'Lecture 21',
        'L22.mov':'Lecture 22',
        'L23.mov':'Lecture 23',
        'L24.mov':'Lecture 24',
        'S10_Q1_P3.mov': 'Static Discipline',
        'S10_Q1_P2.mov': 'Timothy Leary\'s Calendar App',
        'S10_S1_P4.mov': 'Deja Vu',
        'S10_Q2_P2-2.mov': 'Timothy Leary\'s Calendar App (continued)',
        }

    def assign_titles():
        videos = PublicVideo.objects.all()
        for video in videos:
            if video.title == '':
                if video.file_name in titles.keys():
                    video.title = titles[video.file_name]
                    #print "assigning %s as title for file with file_name %s\n" %(titles[video.file_name], video.file_name)
        
    assign_titles()

 
    ## temp topic matcher for testing and development
    topic_assignments = {
        'L03.mov':['CMOSTechnology'],
        'L04.mov':['SynthesisOfCombinationalLogic'],
        'L05.mov':['SequentialLogic'],
        'L06.mov':['FSMs'],
        'L07.mov':['SynchronizationAndMetastability'],
        'L08.mov':['Pipelining'],
        'L09.mov':['Pipelining', 'ModelsOfComputation'],
        'L10.mov':['ProgrammableMachines'],
        'L11.mov':['MachineLanguage'],
        'L14.mov':['BuildingTheBeta'],
        'L15.mov':['MemoryHierarchy'],
        'L16.mov':['Caches'],
        'L17.mov':['VirtualMemory'],
        'L18.mov':['VirtualMachines'],
        'L19.mov':['DevicesInterruptsAndRealTime'],
        'L20.mov':['DevicesInterruptsAndRealTime'],
        'L21.mov':['Semaphores'],
        'L22.mov':['PipelinedBeta'],
        'L23.mov':['PipelinedBeta', 'Pipelining'],
        'L24.mov':['ProgrammableMachines'],
        'S10_Q1_P3.mov': ['TheDigitalAbstraction', 'CMOSTechnology'],
        'S10_Q1_P2.mov': ['BasicsOfInformation'],
        'S10_S1_P4.mov': ['TheDigitalAbstraction', 'GatesAndBooleanLogic'],
        'S10_Q2_P2-2.mov': ['BasicsOfInformation'],
        }

    def match_topics():
        base_url = "http://6004.csail.mit.edu/currentsemester/tutprobs/"
        videos = PublicVideo.objects.all()
        for video in videos:
#            print "(match_topics) working on video: %s" %(video.file_name)
            name=os.path.split(video.file_name)[1]
            if name in topic_assignments.keys():
                topic_match=topic_assignments[name]
                for topic in topic_match:
                    ta = TopicAssignment(video=video, topic=topic)
                #                print "(match_topics) associating %s with %s\n" %(name, topic)
                    ta.save()
                    lp_string = u'%s' %(topic)
                    #print "lp_string = %s\n" %(lp_string)
                    lp_leaf=TUTORIAL_PROBLEM_URLS[lp_string]
                    #print "lp_leaf = %s\n" %(lp_leaf)
                    lp_url=u'%s%s' %(base_url, lp_leaf)
                    lp = LinkedWebPage(name=topic, url=lp_url)
                    lp.topic_assignment=ta
                    lp.save()
                    print "making a linkedWebPage with name=%s and url=%s\n" %(lp.name, lp.url)
    
    print "Matching Topics"
    match_topics()
            


## ----- Quizzes ----- ##

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


## ----- Labs ----- ##

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

