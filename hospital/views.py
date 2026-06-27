from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Appointment


# Add Patient
def add_patient(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        problem = request.POST.get('problem')

        Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            phone=phone,
            problem=problem
        )

        return redirect('/admin/')

    return render(request, 'hospital_app/add_patient.html')


# Patient List
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital_app/patient_list.html', {
        'patients': patients
    })


# Patient Detail
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'hospital_app/patient_detail.html', {
        'patient': patient
    })


# Book Appointment
def book_appointment(request):
    patients = Patient.objects.all()

    if request.method == "POST":
        patient_id = request.POST.get('patient')
        doctor_name = request.POST.get('doctor_name')
        date = request.POST.get('date')
        time = request.POST.get('time')

        patient = Patient.objects.get(id=patient_id)

        Appointment.objects.get_or_create(
            patient=patient,
            appointment_date=date,
            appointment_time=time,
            defaults={'doctor_name': doctor_name}
        )

        return redirect('/appointments/')

    return render(request, 'hospital_app/book_appointment.html', {
        'patients': patients
    })


# Appointment List
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospital_app/appointment_list.html', {
        'appointments': appointments
    })