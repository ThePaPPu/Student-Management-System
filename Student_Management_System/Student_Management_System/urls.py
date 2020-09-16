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

    path('add_course_teacher', AdminViews.add_course_teacher),
    path('add_course_teacher_save', AdminViews.add_course_teacher_save),
    path('manage_course_teacher', AdminViews.manage_course_teacher),
    path('edit_course_teacher/<str:staff_id>', AdminViews.edit_course_teacher),
    path('edit_course_teacher_save', AdminViews.edit_course_teacher_save),


    path('add_course', AdminViews.add_course),
    path('add_course_save', AdminViews.add_course_save),
    path('manage_course', AdminViews.manage_course),

    path('add_student', AdminViews.add_student),
    path('add_student_save', AdminViews.add_student_save),
    path('manage_student', AdminViews.manage_student),

    path('add_subject', AdminViews.add_subject),
    path('add_subject_save', AdminViews.add_subject_save),
    path('manage_subject', AdminViews.manage_subject),


]+static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
