from django.urls import path
from hospital.views import About, Home, Contact, Chatbot, Login, Logout_admin,Index,View_doctor

urlpatterns = [
    path('',Home,name='home'),
    path('about/', About,name='about'),
    path('contact/', Contact,name='contact'),
    path('chatbot/', Chatbot,name='chatbot'),
    path('admin_login/',Login,name='admin_login'),
    path('logout/',Logout_admin,name='logout_admin'),
    path('index/',Index,name='index'),
    path('view_doctor/',View_doctor,name="view_doctor")

]