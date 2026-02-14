from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login
from .models import Doctor
# Create your views here.

def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
         return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()


    d = 0;
    p = 0;
    a = 0;
    for i in doctors:
         d+=1
    for i in patient:
         p+=1
    for i in appointment:
         a+=1
    d1 = {'d':d,'p':p,'a':a}
    return render(request, 'index.html',d1)


def Login(request):
        error=""
        if request.method=='POST':
            u = request.POST['uname']
            p = request.POST['pwd']
            user = authenticate(username=u, password=p)
            try:
                if user.is_staff:
                    login(request, user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        d = {'error': error}   
        return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
         return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
         return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)

def Add_Doctor(request):
        error=""
        if not request.user.is_staff:
            return redirect('login')
        if request.method=='POST':
            n = request.POST['name']
            p = request.POST['contact']
            sp = request.POST['special']
            try:
                
                Doctor.objects.create(name=n, mobile=p, special=sp)
                error=""
            except Exception as e:
                error="yes"
        d = {'error': error}
        return render(request, 'add_doctor.html', d)

def Delete_Doctor(request, pid):
    if not request.user.is_staff:
         return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

# def add_doctor(request):
#     if request.method == "POST":
#         # yahan doctor save ka code hota hai
#         return redirect('view_doctor')   # 👈 YAHAN redirect

#     return render(request, 'add_doctor.html')


# def view_doctor(request):
#     return render(request, 'view_doctor.html')




# def add_doctor(request):
#     error = ""
#     if request.method == "POST":
#         try:
#             Doctor.objects.create(
#                 name=request.POST['name'],
#                 mobile=request.POST['mobile'],
#                 specialization=request.POST['specialization']
#             )
#             error = "no"
#             return redirect('view_doctor')  # 👈 redirect yahin
#         except:
#             error = "yes"

#     return render(request, 'add_doctor.html', {'error': error})


# def view_doctor(request):
#     doctors = Doctor.objects.all()   # 👈 DATA FETCH
#     return render(request, 'view_doctor.html', {'doctors': doctors})

# def add_doctor(request):
#     error = ""
#     if request.method == "POST":
#         try:
#             Doctor.objects.create(
#                 name=request.POST['name'],
#                 mobile=request.POST['mobile'],
#                 special=request.POST['special']
#             )
#             error = "no"
#             return redirect('view_doctor')  # 👈 redirect yahin
#         except:
#             error = "yes"

#     return render(request, 'add_doctor.html', {'error': error})
# def view_doctor(request):
#     doctors = Doctor.objects.all()   # 👈 DATA FETCH
#     return render(request, 'view_doctor.html', {'doctors': doctors})

def View_Patient(request):
    if not request.user.is_staff:
         return redirect('login')
    pat = Patient.objects.all()
    d = {'pat': pat}
    return render(request, 'view_patient.html', d)

def Add_Patient(request):
        error=""
        if not request.user.is_staff:
            return redirect('login')
        if request.method=='POST':
            n = request.POST['name']
            g = request.POST['gender']
            p = request.POST['mobile']
            a = request.POST['address']
            try:
                Patient.objects.create(name=n, gender=g, mobile=p, address=a)
                error="no"
            except:
                error="yes"
        d = {'error': error}
        return render(request, 'add_patient.html', d)

def Delete_Patient(request, pid):
    if not request.user.is_staff:
         return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')



def View_Appointment(request):
    if not request.user.is_staff:
         return redirect('login')
    appoint = Appointment.objects.all()
    d = {'appoint': appoint}
    return render(request, 'view_appointment.html', d)

def Add_Appointment(request):
        error=""
        if not request.user.is_staff:
            return redirect('login')
        doctor1 = Doctor.objects.all()
        patient1 = Patient.objects.all()
        if request.method=='POST':
            d = request.POST['doctor']
            p = request.POST['patient']
            d1 = request.POST['date']
            t = request.POST['time']
            doctor = Doctor.objects.filter(name=d).first()
            patient = Patient.objects.filter(name=p).first()
            try:
                Appointment.objects.create(doctor=doctor,patient=patient,date1=d1,time1=t)
                error="no"
            except:
                error="yes"
        d = {'doctor': doctor1,'patient': patient1,'error': error}
        return render(request, 'add_appointment.html', d)

def Delete_Appointment(request, pid):
    if not request.user.is_staff:
         return redirect('login')
    appointment = Patient.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')
