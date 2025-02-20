
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
account_activation_token = PasswordResetTokenGenerator()

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, 'Password is not matching')
            return render(request, 'signup.html')
        try:
            if User.objects.get(username=email):
                messages.info(request, 'Email is taken')
                return render(request, 'signup.html')
        except User.DoesNotExist:
            user = User.objects.create_user(email, email, password)
            user.is_active = False
            user.save()
            email_subject = "Activate Your Account"
            message = render_to_string('active.html', {
                'user': user,
                'domain': '127.0.0.1:8000',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])
            email_message.send()
            messages.success(request, 'Activate your account by clicking the link in your email')
            return redirect('login')  # settings file added to your mail id and password
    return render(request, "signup.html")

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.info(request, 'Account activated successfully')
            return redirect('login')
        return redirect('activatefail.html')

def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        userpassword = request.POST['pass1']
        myuser = authenticate(username=username, password=userpassword)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('login')
    return render(request, "login.html")

def handlelogout(request):

    logout(request)
    messages.info(request, "Successfully logout")
    return redirect('/auth/login')