import datetime

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student_app.forms import AddStudentForm, EditStudentForm
from student_app.models import CustomUser, Courses, Subjects, Staffs, Students, SessionYearModel


def admin_home(request):
    return render(request, "admin_template/home_content.html")


# Course Teacher

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
            return HttpResponseRedirect(reverse("add_course_teacher"))
        except:
            messages.error(request, "Failed to Add  a Course Teacher")
            return HttpResponseRedirect(reverse("add_course_teacher"))


def manage_course_teacher(request):
    staffs = Staffs.objects.all()
    return render(request, "admin_template/manage_course_teacher_template.html", {"staffs": staffs})


def edit_course_teacher(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(request, "admin_template/edit_course_teacher_template.html", {"staff": staff, "id": staff_id})


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

            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.password = password
            user.save()

            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, "Successfully Edited Course Teacher")
            return HttpResponseRedirect(reverse("edit_course_teacher",kwargs={"staff_id":staff_id}))

        except:
            messages.error(request, "Failed to Edit Course Teacher")
            return HttpResponseRedirect(reverse("edit_course_teacher", kwargs={"staff_id":staff_id}))


# Courses

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
            return HttpResponseRedirect(reverse("add_course"))
        except:
            messages.error(request, "Failed to Add Course")
            return HttpResponseRedirect(reverse("add_course"))


def manage_course(request):
    courses = Courses.objects.all()
    return render(request, "admin_template/manage_course_template.html", {"courses": courses})


def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    return render(request, "admin_template/edit_course_template.html", {"course": course, "id": course_id})


def edit_course_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")

    else:
        course_id = request.POST.get("course_id")
        course_name = request.POST.get("course")

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.save()

            messages.success(request, "Successfully Edited  Course")
            return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id":course_id}))

        except:
            messages.error(request, "Failed to Edit Course")
            return HttpResponseRedirect(reverse("edit_course", kwargs={"course_id":course_id}))


# Students

def add_student(request):
    form = AddStudentForm()
    return render(request, "admin_template/add_student_template.html", {"form": form})


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        form = AddStudentForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            session_year_id = form.cleaned_data["session_year_id"]
            course_id = form.cleaned_data["course"]
            gender = form.cleaned_data["gender"]

            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)

            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                          last_name=last_name, first_name=first_name, user_type=3)
                user.students.gender = gender
                user.students.profile_pic = profile_pic_url
                user.students.address = address
                course_obj = Courses.objects.get(id=course_id)
                user.students.course_id = course_obj
                session_year = SessionYearModel.object.get(id=session_year_id)
                user.students.session_year_id = session_year
                user.save()
                messages.success(request, "Successfully Added a Student")
                return HttpResponseRedirect(reverse("add_student"))

            except:
                messages.error(request, "Failed to Add  a Student")
                return HttpResponseRedirect(reverse("add_student"))

        else:
            form = AddStudentForm(request.POST)
            return render(request, "admin_template/add_student_template.html", {"form": form})


def manage_student(request):
    students = Students.objects.all()
    return render(request, "admin_template/manage_student_template.html", {"students": students})


def edit_student(request, student_id):
    request.session['student_id'] = student_id
    student = Students.objects.get(admin=student_id)

    form = EditStudentForm()
    form.fields['email'].initial = student.admin.email
    form.fields['password'].initial = student.admin.password
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['username'].initial = student.admin.username
    form.fields['address'].initial = student.address
    form.fields['course'].initial = student.course_id.id
    form.fields['gender'].initial = student.gender
    form.fields['session_year_id'].initial = student.session_year_id.id
    form.fields['profile_pic'].initial = student.profile_pic

    return render(request, "admin_template/edit_student_template.html",
                  {"form": form, "id": student_id, "username": student.admin.username})


def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")

    else:
        student_id = request.session.get("student_id")

        if student_id is None:
            return HttpResponseRedirect(reverse("manage_student"))

        form = EditStudentForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            session_year_id = form.cleaned_data["session_year_id"]
            course_id = form.cleaned_data["course"]
            gender = form.cleaned_data["gender"]

            if request.FILES.get('profile_pic', False):
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)

            else:
                profile_pic_url = None

            try:
                user = CustomUser.objects.get(id=student_id)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.username = username
                user.password = password
                user.save()

                student = Students.objects.get(admin=student_id)
                student.address = address
                student.gender = gender
                session_year = SessionYearModel.object.get(id=session_year_id)
                student.session_year_id = session_year
                course = Courses.objects.get(id=course_id)
                student.course_id = course

                if profile_pic_url is not None:
                    student.profile_pic = profile_pic_url

                student.save()

                del request.session['student_id']

                messages.success(request, "Successfully Edited  Student")
                return HttpResponseRedirect(reverse("edit_student", kwargs={"student_id":student_id}))


            except:
                messages.error(request, "Failed to Edit Student")
                return HttpResponseRedirect(reverse("edit_student", kwargs={"student_id":student_id}))

        else:
            form = EditStudentForm(request.POST)
            student = Students.objects.get(admin=student_id)
            return render(request, "admin_template/edit_student_template.html",
                  {"form": form, "id": student_id, "username": student.admin.username})




# Subject

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
            return HttpResponseRedirect(reverse("add_subject"))

        except:
            messages.error(request, "Failed to add Subject")
            return HttpResponseRedirect(reverse("add_subject"))


def manage_subject(request):
    subjects = Subjects.objects.all()
    return render(request, "admin_template/manage_subject_template.html", {"subjects": subjects})


def edit_subject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request, "admin_template/edit_subject_template.html",
                  {"subject": subject, "courses": courses, "staffs": staffs, "id": subject_id})


def edit_subject_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")

    else:
        subject_id = request.POST.get("subject_id")
        subject_name = request.POST.get("subject_name")
        staff_id = request.POST.get("staff")
        course_id = request.POST.get("course")

        try:
            subject = Subjects.objects.get(id=subject_id)
            subject.subject_name = subject_name
            staff = CustomUser.objects.get(id=staff_id)
            subject.staff_id = staff
            course = Courses.objects.get(id=course_id)
            subject.course_id = course
            subject.save()

            messages.success(request, "Successfully Edited Subject")
            return HttpResponseRedirect(reverse("edit_subject",kwargs={"subject_id":subject_id}))

        except:
            messages.error(request, "Failed to Edit Subject")
            return HttpResponseRedirect(reverse("edit_subject",kwargs={"subject_id":subject_id}))


def manage_session(request):
    return render(request, "admin_template/manage_session_template.html")


def add_session_save(request):
    if request.method != "POST":
        return  HttpResponseRedirect(reverse("manage_session"))
    else:
        session_start_year = request.POST.get("session_start")
        session_end_year = request.POST.get("session_end")

        try:
            session_year = SessionYearModel(session_start_year=session_start_year,session_end_year=session_end_year)
            session_year.save()
            messages.success(request, "Successfully Added Session")
            return HttpResponseRedirect(reverse("manage_session"))

        except:
            messages.error(request, "Failed to Added Session")
            return HttpResponseRedirect(reverse("manage_session" ))


