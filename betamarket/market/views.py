from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
import random

User = get_user_model()

@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')

def signupView(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        number = request.POST.get('number')
        password_confirm = request.POST.get('confirm_password')

        if not all([firstname, lastname, email, password, number, password_confirm]):
            messages.error(request, 'Please fill all fields')
            return render(request, 'signup.html')

        if password != password_confirm:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'signup.html')

        verification_code = str(random.randint(100000, 999999))
        my_user = CustomUser.objects.create_user(
            username=email,
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            number=number,
            verification_code=verification_code,
        )
        my_user.is_active = False
        my_user.save()

        send_mail(
            'Your Verification Code',
            f'Hello {firstname},\n\nYour verification code is {verification_code}.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        messages.success(request, "Account created successfully! Check your email for the verification code.")
        return redirect('verify', email=email)

    return render(request, 'signup.html')

def joinView(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.email_verified:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect('home')
            else:
                messages.error(request, "Please verify your email before logging in.")
                return redirect('join')
        else:
            messages.error(request, "Username or Password is incorrect!")

    return render(request, 'join.html')

def verifyView(request, email=None):
    if request.method == 'GET':
        return render(request, 'verify.html', {'email': email})
    
    if request.method == 'POST':
        email = request.POST.get('email')
        code = request.POST.get('verification_code')

        try:
            user = CustomUser.objects.get(email=email)

            if user.verification_code == code:
                user.email_verified = True
                user.is_active = True
                user.verification_code = None
                user.save()
                messages.success(request, 'Email verified successfully! You can now log in.')
                return redirect('login')
            else:
                messages.error(request, 'Invalid verification code.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'User does not exist.')

    return render(request, 'verify.html')

def LogoutPage(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('home')

def ServicesPage(request):
    return render(request, 'services.html')

def contactPage(request):
    return render(request, 'contact.html')

def aboutPage(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def resend_code_view(request):
    user = request.user

    verification_code = str(random.randint(100000, 999999))
    user.verification_code = verification_code
    user.save()

    current_site = get_current_site(request)
    mail_subject = 'Your new verification code'
    message = render_to_string('email_verification.html', {
        'user': user,
        'domain': current_site.domain,
        'code': verification_code,
    })
    send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

    messages.success(request, "A new verification code has been sent to your email.")
    return redirect('verify', email=user.email)

def verify_code_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        code = ''.join([request.POST.get(f'digit{i}') for i in range(1, 7)])

        try:
            user = CustomUser.objects.get(email=email)

            if user.verification_code == code:
                user.email_verified = True
                user.is_active = True
                user.verification_code = None
                user.save()
                messages.success(request, 'Email verified successfully! You can now log in.')
                return redirect('login')
            else:
                messages.error(request, 'Invalid verification code.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'User does not exist.')

    return render(request, 'verify.html')
