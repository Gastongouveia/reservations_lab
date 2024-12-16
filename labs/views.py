from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Lab
from .forms import LabForm

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def add_lab(request):
    if request.method == 'POST':
        form = LabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_labs')
    else:
        form = LabForm()
    return render(request, 'labs/add_lab.html', {'form': form})

def list_labs(request):
    labs = Lab.objects.all()
    return render(request, 'labs/list_labs.html', {'labs': labs})

@login_required
@user_passes_test(is_admin)
def edit_lab(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    if request.method == 'POST':
        form = LabForm(request.POST, instance=lab)
        if form.is_valid():
            form.save()
            return redirect('list_labs')
    else:
        form = LabForm(instance=lab)
    return render(request, 'labs/edit_lab.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_lab(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    if request.method == 'POST':
        lab.delete()
        return redirect('list_labs')
    return render(request, 'labs/delete_lab.html', {'lab': lab})