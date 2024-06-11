from django.urls import path

from . import views

app_name = "userauths"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    # path('register/', views.signup_view, name='register'),
    path('logout/', views.login_view, name="logout"),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
]





