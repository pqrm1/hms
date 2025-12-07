from django.urls import path
from hospital.views import About,Home,Contact,Chatbot

urlpatterns = [
    path('',Home,name='home'),
    path('about/', About,name='about'),
    path('contact/', Contact,name='contact'),
    path('chatbot/', Chatbot,name='chatbot'),
]