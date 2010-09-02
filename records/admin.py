from django.contrib import admin
from usersite.records.models import *
from usersite.tutorials.models import *

class LabRecordAdmin(admin.ModelAdmin):
    list_display=('student', 'lab','score')
    list_filter=('student','lab')
    pass   


class CheckoffMeetingAdmin(admin.ModelAdmin):
    list_display=('student_name', 'lab_number', 'time', 'staff_member')
    fields=('record', 'passed', 'staff_member', 'file')

    def student_name(self, obj):
        return ("%s, %s" %(obj.record.student.last_name, obj.record.student.first_name))

    def student_athena_id(self, record):
        return ("%s" %(obj.record.student.get_profile().athena_id))

    def lab_number(self, obj):
        return obj.record.lab

    pass



#admin.site.register(LabRecord, LabRecordAdmin)
#admin.site.register(QuizGrade)
#admin.site.register(CheckoffMeeting, CheckoffMeetingAdmin)
#admin.site.register(HelpMeeting)
#admin.site.register(LabSubmission)

