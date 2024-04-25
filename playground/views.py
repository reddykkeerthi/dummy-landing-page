from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from landingpage import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
import re

def home(request):

    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        skills = request.POST['skills']
        if User.objects.filter(username = username):
            messages.error(request, "Username already exists! Try another one")
            return redirect('home')
        if User.objects.filter(email = email): 
            messages.error(request, "Email already registered")
            return redirect('home')
        if len(username) >32:
            messages.error(request, "Username should be below 32 characters")
            return redirect('home')
        if len(username) <4:
            messages.error(request, "Username should be above 4 characters")
            return redirect('home')
        if not re.match("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password):
            messages.error(request, "Password must be at least 8 characters, alphanumeric, and include a special character.")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, password)
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your account has been successfully created. We have sent you a confirmation email, Please confirm your email")
        current_site = get_current_site(request)
        subject = "Confirm your email address"
        message = render_to_string('playground/email_confirmation.html', {
            'domain' : current_site.domain, 
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)), 
            'token' : generate_token.make_token(myuser)
        })
        email = EmailMessage(
            subject, 
            message, 
            settings.EMAIL_HOST_USER, 
            [myuser.email]
        )
        email.fail_silently = True
        email.send()
        return redirect('signin')
    
    return render(request, "playground/index.html")

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!! Please login to your account")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')

def signin(request): 
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username = username, password = password)
      if user is not None:
          login(request, user)
          messages.success(request, "You're logged in sucessfully!!")
          return redirect('endpage')
      else: 
          messages.error(request, "Invalid Credentials!")
          return redirect('home')
      
      
    return render(request, "playground/signin.html") 

def endpage(request):
    return render(request, "playground/endpage.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')