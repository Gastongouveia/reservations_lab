from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Teacher
from .forms import TeacherForm
from reservations.models import Reservation

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_teachers')
    else:
        form = TeacherForm()
    return render(request, 'teachers/add_teacher.html', {'form': form})

def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

@login_required
@user_passes_test(is_admin)
def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('list_teachers')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/edit_teacher.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('list_teachers')
    
@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(teacher=request.user.teacher)
    return render(request, 'teachers/my_reservations.html', {'reservations': reservations})
