from django.urls import path
from hospital.views import About, Home, Contact, Chatbot, Login, Logout_admin

urlpatterns = [
    path('',Home,name='home'),
    path('about/', About,name='about'),
    path('contact/', Contact,name='contact'),
    path('chatbot/', Chatbot,name='chatbot'),
    path('admin_login/',Login,name='admin_login'),
    path('logout/',Logout_admin,name='logout_admin')
]