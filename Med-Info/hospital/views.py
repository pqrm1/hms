from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Doctor,Patient,Appointment
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
    doctors=Doctor.objects.all()
    patient=Patient.objects.all()
    appontments=Appointment.objects.all()
    d=0
    p=0
    a=0
    
    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appontments:
        a+=1

    d1={'d':d,'p':p,'a':a}
    return render(request,'index.html',d1)

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

def Add_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('admin_login')
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()
    if request.method == "POST":
        d=request.POST.get('doctor')
        p=request.POST.get('patient')
        da=request.POST.get('date')
        t=request.POST.get('time')
        doctor=Doctor.objects.filter(name=d).first()
        patient=Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date=da,time=t)
            error="no"

        except:
            error="yes"
    d={"doctor":doctor1,"patient":patient1,"error" :error}
    messages.error(request, "All fields are required!")
    return render(request,'add_appointment.html',d)

def View_appointment(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    pat=Appointment.objects.all()
    p={'pat':pat}
    return render(request,'view_appointment.html',p)

def Delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    app=Appointment.objects.get(id=pid)
    app.delete()
    messages.success(request, f"Appointment deleted successfully!")
    return redirect('view_appointment')


def Patient_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        if name and mobile:  # basic validation
            Patient.objects.create(
                name=name,
                gender=gender,
                mobile=mobile,
                address=address or ''  # address optional
            )

    return render(request, 'patient_register.html')

def Doctor_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        special = request.POST.get('special')

        if name and mobile and special:
            Doctor.objects.create(
                name=name,
                mobile=mobile,
                special=special
            )

    return render(request, 'doctor_register.html')