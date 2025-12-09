from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Doctor,Patient
from django.contrib import messages


# Create your views here.

def About(request):
    return render(request, 'about.html')

def Home(request):
    return render(request,'home.html')

def Contact(request):
    return render(request,'contact.html')

def Chatbot(request):
    return render(request,'chatbot.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def Login(request):
    error=""
    if request.method =="POST":
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if User.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={"error":error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('admin_login')

    logout(request)
    return redirect('admin_login')


def View_doctor(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    doc=Doctor.objects.all()
    d={'doc':doc}
    return render(request,'view_doctor.html',d)

def Delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def Add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('admin_login')
    if request.method =="POST":
        n=request.POST['name']
        m=request.POST['mobile']
        sp=request.POST['special']
        try:
            Doctor.objects.create(name=n,mobile=m,special=sp)
            error="no"

        except:
            error="yes"
    d={"error" :error}
    messages.error(request, "All fields are required!")
    return render(request,'add_doctor.html',d)

def View_patient(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    pat=Patient.objects.all()
    p={'pat':pat}
    return render(request,'view_patient.html',p)

def Delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    patient=Patient.objects.get(id=pid)
    patient.delete()
    messages.success(request, f"Patient '{patient.name}' deleted successfully!")
    return redirect('view_patient')

def Add_patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('admin_login')
    if request.method =="POST":
        n=request.POST['name']
        g=request.POST['gender']
        m=request.POST['mobile']
        try:
            Patient.objects.create(name=n,gender=g,mobile=m)
            error="no"

        except:
            error="yes"
    d={"error" :error}
    messages.error(request, "All fields are required!")
    return render(request,'add_patient.html',d)