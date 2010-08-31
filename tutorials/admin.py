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



admin.site.register(UserProfile)
admin.site.register(Quiz)
admin.site.register(Lab)
admin.site.register(PublicVideo, PublicVideoAdmin)
admin.site.register(TopicAssignment)
#admin.site.register(OldQuizVideo, OldQuizVideoAdmin)
#admin.site.register(LabHintVideo, LabHintVideoAdmin)
