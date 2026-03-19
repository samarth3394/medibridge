from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.date.strftime('%Y-%m-%d %H:%M')}"
