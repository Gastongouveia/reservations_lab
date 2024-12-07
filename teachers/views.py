from django.shortcuts import render

# Create your views here.
from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})
