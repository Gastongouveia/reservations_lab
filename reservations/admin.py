from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'lab', 'date', 'start_time', 'end_time', 'approved', 'approved_by', 'canceled_by')
    list_filter = ('date', 'approved')
    search_fields = ('teacher__name', 'lab__name')
