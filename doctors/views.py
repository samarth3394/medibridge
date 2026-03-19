from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def doctor_list(request):
    query = request.GET.get('q')
    if query:
        doctors = Doctor.objects.filter(name__icontains=query)
    else:
        doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

@login_required
def doctor_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        availability = request.POST.get('availability')
        
        Doctor.objects.create(name=name, specialization=specialization, availability=availability)
        messages.success(request, "Doctor added successfully!")
        return redirect('doctor_list')
    
    return render(request, 'doctors/doctor_form.html')
