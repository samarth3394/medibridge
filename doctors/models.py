from django.db import models
from accounts.models import CustomUser

class Doctor(models.Model):
    # Link to user account
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'}, null=True, blank=True)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    availability = models.CharField(max_length=100) # e.g. "Mon-Fri 09:00 AM - 05:00 PM"

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"
