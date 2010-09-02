from django.contrib import admin
from usersite.records.models import *
from usersite.tutorials.models import *


class PublicVideoAdmin(admin.ModelAdmin):
    list_display=('type', 'title', 'file_name','author', 'semester', 'num_favorites')
    list_filter=('type', 'title', 'author', 'semester')

    fields=('type', 'semester', 'author',  'file',  'title')
    
    def num_favorites(self, obj):
        return obj.userprofile_set.count()
    pass


class TopicAssignmentAdmin(admin.ModelAdmin):
    list_display=('topic', 'video')
    list_filter=('topic', 'video')

class LinkedWebPageAdmin(admin.ModelAdmin):
    list_display=('name', 'url', 'pointer_on_page', 'topic_assignment')
    list_filter=('name', 'url', 'topic_assignment')



admin.site.register(UserProfile)
#admin.site.register(Quiz)
#admin.site.register(Lab)
admin.site.register(PublicVideo, PublicVideoAdmin)
admin.site.register(TopicAssignment, TopicAssignmentAdmin)
#admin.site.register(OldQuizVideo, OldQuizVideoAdmin)
#admin.site.register(LabHintVideo, LabHintVideoAdmin)
admin.site.register(Comment)
admin.site.register(LinkedWebPage, LinkedWebPageAdmin)
