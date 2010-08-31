from django.conf.urls.defaults import *
from django.views.generic import list_detail
from django.contrib import databrowse
#from usersite.templates import list_detail 
from django.contrib.auth.views import login, logout, logout_then_login
from usersite.records.models import *
from usersite import views, student_views

#from usersite.student_info import student_info


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


student_list_info = { 
   'queryset': User.objects.filter(is_staff=False), 
   'template_name': 'student_list.html',
}


student_detail_info = {
    'queryset': User.objects.filter(is_staff=False),
    'template_object_name': 'student',
}


urlpatterns = patterns('',
                       # all students
                       (r'^students/$', views.student_list),
                       # admin portal
                       (r'^admin/', include(admin.site.urls)),
                       # trying out databrowse app
                       (r'^databrowse/(,*)', databrowse.site.root),
                       
                       (r'^accounts/login/$', login),
                       (r'^accounts/logout/$', logout_then_login),

                       (r'^accounts/profile/$', student_views.student_portal),

                       

                       # dynamic student detail
                       (r'^students/(?P<athena_id>\w+)/$', views.student_detail),
                       (r'^accounts/records/$', views.student_record),

                       # dynamic student single-lab checkoff record set
                       (r'^students/(?P<athena_id>\w+)/(?P<lab_number>\d{1})/checkoff/$', views.checkoff_records),
                       # dynamic student single-lab help record set
                       (r'^students/(?P<athena_id>\w+)/(?P<lab_number>\d{1})/help/$', views.help_records),
                       # add-form for uploading new interactive content
                       (r'^students/(?P<athena_id>\w+)/(?P<lab_number>\d{1})/add_checkoff/$', views.add_checkoff),
                       # add-form for uploading new interactive content
                       (r'^students/(?P<athena_id>\w+)/(?P<lab_number>\d{1})/add_help/$', views.add_help),

                       #student portal TEST
                       (r'^portals/(?P<athena_id>\w+)/$', student_views.student_portal),

                       #public browser
                       (r'^$', student_views.media_browser),
                       (r'^(?P<public_video_id>\d+)/$', student_views.media_browser),

                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
                        {'document_root': '/home/caitlinj/website/djcode/usersite/media/'}),

   # Example:
    # (r'^usersite/', include('usersite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
