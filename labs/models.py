from django.db import models

# Create your models here.
class Lab(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    resources = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
