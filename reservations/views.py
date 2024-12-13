from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Reservation

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def pending_reservations(request):
    reservations = Reservation.objects.filter(approved=False)
    return render(request, 'reservations/pending_reservations.html', {'reservations': reservations})

@login_required
@user_passes_test(is_admin)
def reservation_list(request):
    reservations = Reservation.objects.select_related('teacher', 'lab').all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})


@login_required
@user_passes_test(is_admin)
def approve_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.approved = True
    reservation.approved_by = request.user
    reservation.save()
    return redirect('pending_reservations')

@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.approved = False
    reservation.canceled_by = request.user
    reservation.save()
    return redirect('reservation_list')