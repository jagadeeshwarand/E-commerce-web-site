from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes,force_text
from django.core.mail import EmailMeassage
from django.conf import settings

# Create your views here.
def signup(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,'paswword is not matching')
            return render(request,'auth.signup.html')
        try:
            if User.objects.get(username=email):
                return  messages.info(request,'Email is taken')
                return render(request,'auth/signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()
        email_subject="Active Your Acccount"
        message = render_to_string('active.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user)})
            email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
            email_message.send()
            messages.success(request,'Activate your account by clicking the link in your email')
            return redirect('/auth/login')


    return render(request,"authentication/signup.html")

def handlelogin(request):
    return render(request,"authentication/login.html")

def handlelogout(request):
    return redirect('/auth/login')