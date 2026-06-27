from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add-patient/', views.add_patient, name='add_patient'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patient/<int:patient_id>/', views.patient_detail, name='patient_detail'),

    # Appointment
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.appointment_list, name='appointment_list'),

    # ✏️ Edit + 🗑️ Delete (NEW ADD HERE)
    path('patient/edit/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    path('patient/delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),
]