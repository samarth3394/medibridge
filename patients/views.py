from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def patient_list(request):
    query = request.GET.get('q')
    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

@login_required
def patient_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        history = request.POST.get('medical_history')
        
        Patient.objects.create(name=name, age=age, gender=gender, contact=contact, medical_history=history)
        messages.success(request, "Patient added successfully!")
        return redirect('patient_list')
    
    return render(request, 'patients/patient_form.html')

@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, "Patient deleted.")
        return redirect('patient_list')
    return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})
