from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all().order_by('date')
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

@login_required
def appointment_create(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        
        patient = get_object_or_404(Patient, id=patient_id)
        doctor = get_object_or_404(Doctor, id=doctor_id)
        
        Appointment.objects.create(patient=patient, doctor=doctor, date=date)
        messages.success(request, "Appointment booked successfully!")
        return redirect('appointment_list')
        
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'appointments/appointment_form.html', {'patients': patients, 'doctors': doctors})

@login_required
def appointment_cancel(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = 'cancelled'
    appointment.save()
    messages.success(request, "Appointment cancelled.")
    return redirect('appointment_list')
