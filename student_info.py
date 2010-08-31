from django.template import TemplateDoesNotExist
from django.views.generic import list_detail
from usersite.records.models import Student

def student_info(request):
    return list_detail.object_list(
        request,
        queryset = Student.objects.all(),
        template_name = 'student_list.html',
        template_object_name = 'student',
        )
