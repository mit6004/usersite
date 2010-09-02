from django.contrib import databrowse, admin
from django.contrib.auth.models import User
## Using the django admin user model
from django.db import models
from django.conf import settings
from tutorials.enums import *
import datetime, os


IMAGE_TYPE_LIST=['.jpg', '.gif', '.png', ]
VIDEO_TYPE_LIST=['.mov', '.flv', '.mp4']


class Quiz(models.Model):
    num = models.IntegerField(max_length=1, choices=QUIZ_CHOICES)
    quiz_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
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


class MediaSubmission(models.Model):
    description = models.CharField(blank=True, max_length=200)
    title = models.CharField(blank=True, max_length=200)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    file_name=models.CharField(max_length=64, blank=True)

    class Meta:
        abstract = True
        ## want to be able to use this for PublicDocument too


def get_upload_location(instance, filename):
    #return '%sMisc/%s' %(settings.MEDIA_ROOT, self.semester)
    ret = os.path.join('%s' %(instance.author), 
                       instance.type, 
                       instance.semester, 
                       filename)
#    ret +='/'
    return ret


## ned to test this
class StaffFavoriteManager(models.Manager):
    def get_query_set(self):
        return super(StaffFavoriteManager, self).get_query_set().filter(staff_favorite__gt=0)


class PublicVideo(MediaSubmission):
    author = models.ForeignKey(User)
    type = models.CharField(max_length=7, choices=VIDEO_CHOICES)
    # in quotes because 'User' hasn't been defined yet
    semester= models.CharField(max_length=3, choices=SEMESTER_CHOICES)
    ## Can create an Intermediate model -Relevance- that one can define 
    ## more characteristics for. by adding a through='Relevance' attribute
    ## to the above -topic- definition.
    file = models.FileField(upload_to = get_upload_location)
    
    def __unicode__(self):
        return u' \"%s\" by %s (%s) ' %(self.title, self.author, self.semester)
    ## For admin site, there is a link on top right that says 
    ## "view on site" and allows the file itself to be seen the 
    ## the way it's being "served" which, for development purposes,
    ## is through "static.media.serve
    def get_absolute_url(self):
        print "running get_absolute_url"
        return 'http://128.30.65.41:8000/site_media/%s' %(self.upload_location)

    def _get_upload_location(self):
#        print "(_get_upload_location) self.file_name = %s\n" %(self.file_name)
        return get_upload_location(self, self.file_name)
    upload_location=property(_get_upload_location)

    def _get_filesystem_location(self):
        fs_path = os.path.join(settings.MEDIA_ROOT, self.upload_location)
        print "(_get_filesystem_location) fs_path = %s\n" %(fs_path)
        return fs_path
    file_system_location=property(_get_filesystem_location)

    def _num_staff_favorites(self):
        favoriter_set = self.userprofile_set.all()
        staff_favorite = 0
        for favoriter_profile in favoriter_set:
            staff_favorite += favoriter_profile.user.is_staff
        return staff_favorite
    staff_favorite = property(_num_staff_favorites)

    def save(self):
        if self.file:
            if not self.file_name:
                # careful not to assign this in all cases but only when another name is not 
                # specified. otherwise you can't override it!
                self.file_name=self.file.name
            upload_location = get_upload_location(self, self.file_name)
#   
            print "(publicVideo.save) writing %s upload_location: %s" %(self.file_name, upload_location)
            super(PublicVideo, self).save()
        
    
    
    def _is_video(self):
        return os.path.splitext(self.file_name)[1] in VIDEO_TYPE_LIST
    is_video = property(_is_video)

    def _is_image(self):
        return os.path.splitext(self.file_name)[1] in IMAGE_TYPE_LIST
    is_image = property(_is_image)

    objects = models.Manager()
    staff_favorites = StaffFavoriteManager()


def open_location(filesystem_location, **kwargs):
    # Makes the directory structure in the MEDIA_ROOT directory if not there already
    # for some reason it works to create the directories correctly like this
    # but not without the following two lines.
    print "(open_location) filesystem_location = %s\n" %(filesystem_location)
    if not instance.file_name:
        instance.file_name=instance.file.name
    print "(save_video) instance.file_name = %s\n" %(instance.file_name)
#    instance.save()
    filesystem_path = "%s%s" %(settings.MEDIA_ROOT, instance.upload_location)
    try: os.makedirs(filesystem_path)
    except: print "(save_video) trying to open path for %s" %(instance.file_name)
    filesystem_location = os.path.join(filesystem_path, instance.file_name)
#    open_location(filesystem_location)
    destination = open(filesystem_location, 'wb+')
    print "(save_video) opened location %s\n" %(filesystem_location)
    destination.close()



## Annotations ##


class Annotation(models.Model):
    video = models.ForeignKey(PublicVideo)
    start_time = models.FloatField(default=0.0)
    stop_time = models.FloatField(default=0.0)
    # OFFSET from beginning of video

class Comment(Annotation):
    user=models.ForeignKey(User)
    text=models.TextField()
    
    def __unicode__(self):
        return u'%s: %s' %(self.video, self.topic)
    

    

class TopicAssignment(Annotation):
    ## inherits the percentage range of completion through document
    topic = models.CharField(max_length=128, choices=TOPIC_CHOICES)
    ## constrained to match the choices of topic made available 
    ## for study materials under the tutorial problem section of 
    ## the 6.004 website. 
    
    def __unicode__(self):
        return u'%s: %s' %(self.video, self.topic)

    def _get_video_author(self):
        return self.video.author
    author=property(_get_video_author)

    def _get_video_type(self):
        return self.video.type
    type=property(_get_video_type)

    def _get_video_semester(self):
        return self.video.semester
    semester=property(_get_video_semester)
    
    num_staff_favorites=models.IntegerField(default=0)


    def set_num_staff_favorites(self, value):
        self.num_staff_favorites=value
    
    def set_num_student_favorites(self, value):
        self.num_student_favorites=value

    def get_num_staff_favorites(self):
        return self.userprofile_set.filter(user__is_staff=True).count()
#    num_staff_favorites=property(get_num_staff_favorites)

    def get_num_student_favorites(self):
        return self.userprofile_set.filter(user__is_staff=False).count()
#    num_student_favorites=property(get_num_student_favorites)



class LinkedWebPage(models.Model):
    name=models.CharField(max_length=50, default="")
    url=models.URLField(default="http://6004.csail.mit.edu/currentsemester/")
    topic_assignment = models.ForeignKey(TopicAssignment)
    pointer_on_page=models.CharField(max_length=50, default="")




## ------- USER STUFF ------ ##

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    ## User is required to have User.get_profile() work.
    ## It has to be named "user" and refer to a "User" ForeignKey
    ## See Django Book ch 12 for more info
    athena_id = models.CharField(max_length=8, primary_key=True)
    student_id = models.IntegerField(max_length=9, unique=True, null=True, blank=True)
    favorites = models.ManyToManyField(TopicAssignment, null=True, blank=True)

    def __unicode__(self):
        return self.athena_id

## -- SIGNAL UTILS -- ##

## a signal is sent when a User object is being saved.
## Immediately after the User is saved, we want to ensure
## that there is a corresponding UserProfile object created
## with that User as a ForeignKey... 
## see "Signals" documentation for more info

def make_profile(sender, instance, **kwargs):
    if (UserProfile.objects.filter(pk=instance.username).count() == 0):
        # If there is not already an instance
        profile=UserProfile(athena_id=instance.username)
        profile.user = instance
        # Can't get this method to save the Student ID so it is 
        # IMPORTANT to make sure that the student_id is consitently
        # set in the profile manually after the User is saved, and this
        # profile gets created.
        profile.save()
    instance.is_active=True
    ## set is_active=True at time of creation. Can be manually reset. Default,

def databrowse_register(sender, **kwargs):
    databrowse.site.register(sender)


def admin_register(sender, **kwargs):
    admin.site.register(sender)


# --- SIGNALS --- ##
models.signals.post_save.connect(make_profile, sender=User)
models.signals.class_prepared.connect(databrowse_register)




#class StaffMember(User):
#    type = models.CharField(max_length=8, choices=STAFF_CHOICES)
  

#class Student(User):
#    student_id = models.IntegerField(max_length=9, unique=True)
#    class_year = models.IntegerField(max_length=4)

    

 


