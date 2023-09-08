from django.shortcuts import render
import os
from django.http import FileResponse
from . models import Contact
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'index.html')

def start_quiz(request):
    return render(request,'projects/Start_Quiz.html')

def main_quiz(request):
    return render(request,'projects/mainquiz.html')

def cal(request):
    return render(request,'projects/Calculator.html')

def resume(request):
    filepath=os.path.join('home/templates','Resume_Chinmay.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

@csrf_exempt
def contact(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        phone_number=request.POST['phone_number']
        hire_for=request.POST['hire_for']
        Contact.objects.create(name=name,email=email,message=message,phone=phone_number,hire_for=hire_for)
        owner_email=settings.EMAIL_HOST_OWNER
        recipient_list = [owner_email]
        subject = "Request from Portfolio"
        email_from = settings.EMAIL_HOST_USER

        message_body = f"new Request  by {name}.\n'Mobile Number : '{phone_number} \n'Email: '{email} \n'Hire For: '{hire_for}  \n'Message : '{message} \n" 
        send_mail(subject, message_body, email_from, recipient_list, fail_silently=True)
        messages.success(request,'Message Send')
        return render(request,'index.html')
    else:
        return render(request,'index.html')

@csrf_exempt  
def contact_light(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        phone_number=request.POST['phone_number']
        hire_for=request.POST['hire_for']
        Contact.objects.create(name=name,email=email,message=message,phone=phone_number,hire_for=hire_for)
        owner_email=settings.EMAIL_HOST_OWNER
        recipient_list = [owner_email]
        subject = "Request from Portfolio"
        email_from = settings.EMAIL_HOST_USER

        message_body = f"new Request  by {name}.\n'Mobile Number : '{phone_number} \n'Email: '{email} \n'Hire For: '{hire_for}  \n'Message : '{message} \n" 
        send_mail(subject, message_body, email_from, recipient_list, fail_silently=True)
        messages.success(request,'Message Send')
        return render(request,'light.html') 
    else: 
        return render(request,'light.html')   
    

def light(request):
    return render(request,'light.html')    