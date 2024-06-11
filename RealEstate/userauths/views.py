from django.core.mail import send_mail
from django.contrib.auth import logout as v_logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .forms import LoginForm

from .models import User

def send_otp(email):
    otp = get_random_string(6, allowed_chars='0123456789')
    send_mail(
        'Your OTP Code',
        f'Your OTP code is {otp}',
        'from@example.com',
        [email],
        fail_silently=False,
    )
    return otp

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            otp = send_otp(email)
            request.session['registration_data'] = {
                'email': email,
                'password': password,
                'otp': otp,
            }
            messages.success(request, "An OTP has been sent to your email")
            return redirect('userauths:verify_otp')
        else:
            messages.error(request, "Both email and password are required")
            return render(request, "userauths/register.html")

    return render(request, "userauths/register.html")

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        registration_data = request.session.get('registration_data')

        if registration_data and registration_data.get('otp') == otp:
            user = User.objects.create_user(
                username=registration_data['email'],  # Assuming username is same as email
                email=registration_data['email'],
                password=registration_data['password']
            )
            messages.success(request, "Successfully registered, please login")
            return redirect("userauths:login")
        else:
            messages.error(request, "Invalid OTP")
            return render(request, 'userauths/verify_otp.html')
    
    # Ensure user variable is defined even for GET requests or if POST fails
    user = None
    return render(request, 'userauths/verify_otp.html', {'user': user})

# def register(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         otp = send_otp(email)
#         request.session['registration_data'] = {
#             'email': email,
#             'password': password,
#             'otp': otp,
#         }
#         messages.success(request, "An otp has been sent to your email")
#         # return JsonResponse({'message': 'OTP sent to your email'}, status=200)
#         return redirect(request, 'userauths:verify_otp')
#     return render(request, "userauths/register.html")
    
   

# def verify_otp(request):
#     if request.method == 'POST':
#         otp = request.POST['otp']
#         registration_data = request.session.get('registration_data')
#         if registration_data['otp'] == otp:
#             user = User.objects.create_user(
#                 email=registration_data['email'],
#                 password=registration_data['password']
#             )
#             messages.success(request, "successfully registered, login")
#             return redirect("userauths:login")
#             # return JsonResponse({'message': 'User registered successfully'}, status=200)
#         # return JsonResponse({'message': 'Invalid OTP'}, status=400)
#     return render(request, 'userauths/verify_otp.html')

def logout(request):
    v_logout(request)
    messages.warning(request, "Logged out.")
    return redirect("core:index")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}")
            return redirect("core:index")
        else:
            messages.error(request, "Login failed. Please check your credentials and try again.")
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "userauths/login.html", context)

# def login_view(request):
#     if request.method == "POST":
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             messages.success(request, f"Welcome, '{user}'")
#             return redirect("core:index")

#     else:
#         form = LoginForm()
#     context = {
#         "form": form
#     }
#     return render(request, "userauths/login.html", context)

