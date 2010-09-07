from django.conf.urls.defaults import *
from django.views.generic import list_detail
from django.contrib import databrowse
#from usersite.templates import list_detail 
from django.contrib.auth.views import login, logout, logout_then_login
from usersite.records.models import *
from usersite import views, student_views, staff_views

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

#databrowse.site.register(PublicVideo)
#databrowse.site.register(TopicAssignment)
#databrowse.site.register(User)



urlpatterns = patterns('',
                       # all students
                       #(r'^students/$', views.student_list),
                       # admin portal
                       (r'^admin/', include(admin.site.urls)),
                       # trying out databrowse app
                       (r'^databrowse/(.*)', databrowse.site.root),
                       
                       (r'^accounts/login/$', login),
                       (r'^accounts/logout/$', logout_then_login),
                       
                       # template: /templates/tutorials/browse.html
                       (r'^accounts/profile/$', student_views.student_portal),

                       # staff editing and topic assigning page
                       (r'^topic_assign/(?P<video_id>\d+)/$', staff_views.preview_and_set_topic),
                       (r'^upload_video/$', staff_views.upload_video),

                       (r'^landing/$', views.landing),

                       # web of links
                       (r'^web/show_media/(?P<ta_id>\d+)/$', views.show_media),
                       (r'^web/show_for_topic/(?P<topic>\w+)/$', views.show_by_topic),
                       (r'^web/show_for_author/(?P<author_username>\w+)/$', views.show_by_author),
                       (r'^web/show_for_semester/(?P<semester>\w+)/$', views.show_by_semester),
                       (r'^web/show_for_type/(?P<type>\w+)/$', views.show_by_type),
                       

                       #student portal TEST
                       (r'^portals/(?P<athena_id>\w+)/$', student_views.student_portal),

                       #public browser
                       (r'^$', student_views.browse),
                       (r'^(?P<topic_snippet_id>\d+)/$', student_views.browse),
                       (r'^(?P<topic_snippet_id>\d+)/(?P<is_favorite>\w+)/$', student_views.browse),
                       (r'^(?P<topic_snippet_id>\d+)/(?P<is_favorite>\w+)/(?P<query_string>\w+)/$', student_views.browse),

                       (r'^(?P<topic_snippet_id>\d+)/(?P<is_favorite>\w+)/(?P<show_favorites>\w+)/$', 
                        student_views.student_portal),
                       (r'^(?P<topic_snippet_id>\d+)/(?P<is_favorite>\w+)/(?P<show_favorites>\w+)/(?P<query_string>\w+)/$', 
                        student_views.student_portal),


                       # static serve
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
                        {'document_root': '/home/caitlinj/website/djcode/usersite/media/'}),


                       # tutorial problems
                       (r'^tutprobs/(?P<topic>\w+)/$', views.tutorial_by_topic),
                       (r'^tutprobs/(?P<topic>\w+)/(?P<linked_problem_id>\d+)/$', views.tutorial_by_id),
                       

                       # dynamic student detail
                       #(r'^students/(?P<athena_id>\w+)/$', views.student_detail),
                       #(r'^accounts/records/$', views.student_record),
                       # dynamic student single-lab checkoff record set
                       #(r'^students/(?P<athena_id>\w+)/(?P<lab_number>\d{1})/checkoff/$', views.checkoff_records),
                       # dynamic student single-lab help record set
                       #(r'^students/(?P<athena_id>\w+)/(?P<lab_number>\d{1})/help/$', views.help_records),
                       # add-form for uploading new interactive content
                       #(r'^students/(?P<athena_id>\w+)/(?P<lab_number>\d{1})/add_checkoff/$', views.add_checkoff),
                       # add-form for uploading new interactive content
                       #(r'^students/(?P<athena_id>\w+)/(?P<lab_number>\d{1})/add_help/$', views.add_help),

                       # Example:
                           # (r'^usersite/', include('usersite.foo.urls')),
                       
                       # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
                       # to INSTALLED_APPS to enable admin documentation:
                           # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       # Uncomment the next line to enable the admin:
                           # (r'^admin/', include(admin.site.urls)),
                       )
