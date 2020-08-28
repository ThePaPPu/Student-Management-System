from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Student_Management_System import settings
from student_app import views, AdminViews

urlpatterns = [
    #path('', views.DemoView),
    path('', views.LoginView),
    path('doLogin', views.doLogin),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.LogoutUser),
    path('admin_home', AdminViews.admin_home),
    path('add_staff', AdminViews.add_staff),
    path('add_staff_save', AdminViews.add_staff_save),
    path('add_course', AdminViews.add_course),
    path('add_course_save', AdminViews.add_course_save),


]+static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
