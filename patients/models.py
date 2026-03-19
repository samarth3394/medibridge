from django.db import models
from accounts.models import CustomUser

class Patient(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    
    # Link to user account
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'patient'}, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact = models.CharField(max_length=15)
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
