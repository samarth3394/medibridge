from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

@login_required
def home(request):
    context = {
        'total_patients': Patient.objects.count(),
        'total_doctors': Doctor.objects.count(),
        'total_appointments': Appointment.objects.count(),
        'recent_appointments': Appointment.objects.all().order_by('-date')[:5]
    }
    return render(request, 'home.html', context)
