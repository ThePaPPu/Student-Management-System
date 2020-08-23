from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Student_Management_System import settings
from student_app import views

urlpatterns = [
    path('', views.AdminView),
    path('login', views.LoginView),
    path('doLogin', views.doLogin),


]+static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
