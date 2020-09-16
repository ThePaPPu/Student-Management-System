import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_app.models import CustomUser, Courses, Subjects, Staffs, Students


def admin_home(request):
    return render(request, "admin_template/home_content.html")


def add_course_teacher(request):
    return render(request, "admin_template/add_course_teacher_template.html")


def add_course_teacher_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request, "Successfully Added a Course Teacher")
            return HttpResponseRedirect("/add_course_teacher")
        except:
            messages.error(request, "Failed to Add  a Course Teacher")
            return HttpResponseRedirect("/add_course_teacher")


def add_course(request):
    return render(request, "admin_template/add_course_template.html")


def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        course = request.POST.get("course")

        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Successfully Added Course")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request, "Failed to Add Course")
            return HttpResponseRedirect("/add_course")


def add_student(request):
    courses = Courses.objects.all()
    return render(request, "admin_template/add_student_template.html", {"course": courses})


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id = request.POST.get("course")
        gender = request.POST.get("gender")

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=3)
            user.students.gender = gender
            user.students.profile_pic = ""
            user.students.address = address
            course_obj = Courses.objects.get(id=course_id)
            user.students.course_id = course_obj

            # start_date=datetime.datetime.strptime(session_start,'%d-%m-%y').strftime('%Y-%m-%d')

            # end_date = datetime.datetime.strptime(session_end, '%d-%m-%y').strftime('%Y-%m-%d')

            user.students.session_start_year = session_start
            user.students.session_end_year = session_end
            user.save()
            messages.success(request, "Successfully Added a Student")
            return HttpResponseRedirect("/add_student")

        except:
            messages.error(request, "Failed to Add  a Student")
            return HttpResponseRedirect("/add_student")


def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request, "admin_template/add_subject_template.html", {"staffs": staffs, "courses": courses})


def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        staff_id = request.POST.get("staff")
        staff = CustomUser.objects.get(id=staff_id)

        try:
            subject = Subjects(subject_name=subject_name, course_id=course, staff_id=staff)
            subject.save()
            messages.success(request, "Successfully Added Subject")
            return HttpResponseRedirect("/add_subject")

        except:
            messages.error(request, "Failed to add Subject")
            return HttpResponseRedirect("/add_subject")


def manage_course_teacher(request):
    staffs = Staffs.objects.all()
    return render(request, "admin_template/manage_course_teacher_template.html", {"staffs": staffs})


def manage_student(request):
    students = Students.objects.all()
    return render(request, "admin_template/manage_student_template.html", {"students": students})


def manage_course(request):
    courses = Courses.objects.all()
    return render(request, "admin_template/manage_course_template.html", {"courses": courses})


def manage_subject(request):
    subjects = Subjects.objects.all()
    return render(request, "admin_template/manage_subject_template.html", {"subjects": subjects})


def edit_course_teacher(request,staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    return render(request, "admin_template/edit_course_teacher_template.html", {"staff":staff})


def edit_course_teacher_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")

    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")

        try:

            user=CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.password=password
            user.save()

            staff_model=Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.save()

            messages.success(request, "Successfully Edited Course Teacher")
            return HttpResponseRedirect("/edit_course_teacher/"+staff_id)

        except:
            messages.error(request, "Failed to Edit Course Teacher")
            return HttpResponseRedirect("/edit_course_teacher/"+staff_id)
