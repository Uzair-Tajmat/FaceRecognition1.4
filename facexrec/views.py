from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Student
from .models import Present
from .models import Report
from .forms import StudentForm
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import Image, ImageFilter
from django.db import connection
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime



# Create your views here.
# SuperUser Uzma Password UzairUzma

def HomePage(request):
    return render(request,'home.html')


def aboutus(request):
    return render(request,'about_us.html')



def SignUp(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        passwd1=request.POST.get('password1')
        passwd2=request.POST.get('password2')
        
        if passwd1!=passwd2:
            return HttpResponse("Password do not match ")

        else:
            my_user=User.objects.create_user(uname,email,passwd1)
            my_user.save()

        return redirect('login')
    return render(request,'registration.html')

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('first')
        else:
            return HttpResponse('Username and password is incorrect!!!')

    return render(request,'login.html')

@login_required(login_url='home')
def first(request):
    return render(request,'first.html')






# @login_required(login_url='home')
def imageregister(request):
    # global myLIst
    # global registered_encodings
    # global imglist
    # global classNames
  
    form=StudentForm()
    context = {'form':form}
    if request.method=="POST":
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

                        

        
    return render(request,'imageregister.html',context)



def TYCMA(request):
    return render(request,'TYCMA.html')

def student_table(request):
    context={'studenttable':Student.objects.filter(div_id=5)}
    return render(request,'studenttable.html',context)
    



def Logout(request):
    logout(request)
    return redirect('home')


#All down here is code for face recognition and marking attendance
path = 'media/encode'
imglist =[]
classNames =[]
myLIst = os.listdir(path= path)
registered_encodings = None
for cls in myLIst:
    curImg = cv2.imread(f'{path}/{cls}')
    imglist.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
def findencode(imgList):
    encodelist = []
    for imgl in imglist:
        imgl =  cv2.cvtColor(imgl,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(imgl)[0]

        encodelist.append(encode)

    return encodelist
registered_encodings = findencode(imglist)

context=[]

name=None
student_data=None
def mark(request):
    global imglist
    global registered_encodings
    global name
    global student_data
    global context
    if request.method=="POST":
        
        
        cap = cv2.VideoCapture(0)
        address=("https://192.168.182.41:8080/shot.jpg")
        cap.open(address)
        
       
        while True:
            if cap.isOpened():
                success,imglist =cap.read()
            else:
                success = False

            imgS = cv2.cvtColor(imglist, cv2.COLOR_BGR2RGB)
            cap.release()

            facCurrentLoc = face_recognition.face_locations(imgS)
            encodeCurrentLoc = face_recognition.face_encodings(imgS,facCurrentLoc)
            

            for encodeface,faceLoc in zip(encodeCurrentLoc,facCurrentLoc):
                matches = face_recognition.compare_faces(registered_encodings,encodeface)
                facedis = face_recognition.face_distance(registered_encodings,encodeface)

                matchindex = np.argmin(facedis)

                if matches[matchindex]:
                    name = classNames[matchindex].upper()
                    print(name)
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO facexrec_present (enroll) VALUES (%s)",[name])
                    cursor.close()

                qs1=Student.objects.values_list('enroll')
                qs2=Present.objects.values_list('enroll')
                student_data=qs2.intersection(qs1)
                context=Student.objects.filter(enroll__in=student_data).values
                
            return render(request,'attendance.html',{'studenttable':context})

def download(request):
    now=datetime.datetime.now()
    global student_data
    attendance=Student.objects.filter(enroll__in=student_data).values
    template_path = 'Download.html'
    context = {'attendance':attendance}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Attendance.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
       
    print(pisa_status)
    Present.objects.all().delete()
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def addAttendance(request):
    context={'addAttendance':Student.objects.filter(year_id=4)}
    return render(request,"addAttendance.html",context)

 

def reportissue(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        discription=request.POST.get('discription')
        data=Report(name=name,email=email,discription=discription)
        data.save()

    return render(request,"reportissue.html")


def downloadAttendance(request):
    return render(request,"downloadAttendance.html")
