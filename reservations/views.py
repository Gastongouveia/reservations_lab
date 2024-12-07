from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation

def reservation_list(request):
    reservations = Reservation.objects.select_related('teacher', 'lab').all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

@login_required
def approve_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.approved = True
    reservation.approved_by = request.user
    reservation.save()
    return redirect('reservation_list')

@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.approved = False
    reservation.canceled_by = request.user
    reservation.save()
    return redirect('reservation_list')