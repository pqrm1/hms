from django.urls import path
from hospital.views import (About, Home, Contact, Chatbot, Login, Logout_admin,Index,View_doctor,
                            Delete_doctor,View_patient,Delete_patient,Add_doctor,Add_patient,
                            Add_appointment,View_appointment,Delete_appointment,
                            Patient_register,Doctor_register)

urlpatterns = [
    path('',Home,name='home'),
    path('about/', About,name='about'),
    path('contact/', Contact,name='contact'),
    path('chatbot/', Chatbot,name='chatbot'),
    path('admin_login/',Login,name='admin_login'),
    path('logout/',Logout_admin,name='logout_admin'),
    path('index/',Index,name='index'),
    path('view_doctor/',View_doctor,name="view_doctor"),
    path('delete_doctor(?p<int:pid>)/',Delete_doctor,name="delete_doctor"),
    path('add_doctor/',Add_doctor,name="add_doctor"),
    path('view_patient/',View_patient,name="view_patient"),
    path('delete_patient(?p<int:pid>)/',Delete_patient,name="delete_patient"),
    path('add_patient/',Add_patient,name="add_patient"),
    path('add_appointment/',Add_appointment,name="add_appointment"),
    path('view_appointment/',View_appointment,name="view_appointment"),
    path('delete_appointment(?p<int:pid>)/',Delete_appointment,name="delete_appointment"),
    path('patient_register/', Patient_register, name='patient_register'),
    path('doctor_register/', Doctor_register, name='doctor_register'),

]