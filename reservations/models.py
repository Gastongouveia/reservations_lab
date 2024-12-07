from django.contrib.auth.models import User
from django.db import models
from teachers.models import Teacher
from labs.models import Lab

class Reservation(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="reservations")
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name="reservations")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="approved_reservations")
    canceled_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="canceled_reservations")

    def __str__(self):
        return f"Reservation by {self.teacher} for {self.lab} on {self.date}"