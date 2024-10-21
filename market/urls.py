# urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('join/', views.joinView, name='join'),
    path('signup/', views.signupView, name='signup'),
    path('verify/<str:email>/', views.verifyView, name='verify'),
    path('verify_code/', views.verify_code_view, name='verify_code'),
    path('resend_code/', views.resend_code_view, name='resend_code'),
    path('logout/', views.LogoutPage, name='logout'),
    path('services/', views.ServicesPage, name='services'),
    path('contact/', views.contactPage, name='contact'),
    path('about/', views.aboutPage, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='join.html'), name='login'),
]
