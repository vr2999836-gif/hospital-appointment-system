from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient, Appointment, Doctor


# Home
@login_required
def home(request):
    total_patients = Patient.objects.count()
    total_appointments = Appointment.objects.count()

    return render(request, 'hospital_app/home.html', {
        'total_patients': total_patients,
        'total_appointments': total_appointments,
    })


# Add Patient
@login_required
def add_patient(request):
    if request.method == "POST":
        Patient.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
            phone=request.POST.get('phone'),
            problem=request.POST.get('problem')
        )
        return redirect('/patients/')

    return render(request, 'hospital_app/add_patient.html')
def patient_list(request):
    query = request.GET.get('q')

    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()

    return render(request, 'hospital_app/patient_list.html', {
        'patients': patients
    })




# Patient Detail
@login_required
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    return render(request, 'hospital_app/patient_detail.html', {
        'patient': patient
    })


# Book Appointment
@login_required
def book_appointment(request):
    patients = Patient.objects.all()

    if request.method == "POST":
        patient = Patient.objects.get(id=request.POST.get('patient'))

        doctor_name = request.POST.get('doctor_name')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Duplicate Check
        exists = Appointment.objects.filter(
            patient=patient,
            doctor_name=doctor_name,
            appointment_date=date,
            appointment_time=time
        ).exists()

        if exists:
            return render(request, 'hospital_app/book_appointment.html', {
                'patients': patients,
                'error': 'This appointment already exists.'
            })

        Appointment.objects.create(
            patient=patient,
            doctor_name=doctor_name,
            appointment_date=date,
            appointment_time=time
        )

        return redirect('/appointments/')

    return render(request, 'hospital_app/book_appointment.html', {
        'patients': patients
    })


# Appointment List
@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()

    return render(request, 'hospital_app/appointment_list.html', {
        'appointments': appointments
    })


# Edit Patient
@login_required
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == "POST":
        patient.name = request.POST.get('name')
        patient.age = request.POST.get('age')
        patient.gender = request.POST.get('gender')
        patient.phone = request.POST.get('phone')
        patient.problem = request.POST.get('problem')
        patient.save()

        return redirect('/patients/')

    return render(request, 'hospital_app/edit_patient.html', {
        'patient': patient
    })


# Delete Patient
@login_required
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.delete()

    return redirect('/patients/')

