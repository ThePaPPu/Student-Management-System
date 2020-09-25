from django import forms

from student_app.models import Courses


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))

    password = forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))

    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class":"form-control"}))

    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class":"form-control"}))

    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    courses = Courses.objects.all()
    course_list = []
    for course in courses:
        small_course = (course.id, course.course_name)
        course_list.append(small_course)

    course = forms.ChoiceField(label="Course", choices=course_list,
                               widget=forms.Select(attrs={"class":"form-control"}))

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    gender = forms.ChoiceField(label="Gender", choices=gender_choice,
                               widget=forms.Select(attrs={"class":"form-control"}))

    session_start = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))

    session_end = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))

    profile_pic = forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}))





class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}), required=False)

    password = forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}), required=False)

    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class":"form-control"}), required=False)

    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class":"form-control"}), required=False)

    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}), required=False)

    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}), required=False)

    courses = Courses.objects.all()
    course_list = []
    for course in courses:
        small_course = (course.id, course.course_name)
        course_list.append(small_course)

    course = forms.ChoiceField(label="Course", choices=course_list,
                               widget=forms.Select(attrs={"class":"form-control"}), required=False)

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    gender = forms.ChoiceField(label="Gender", choices=gender_choice,
                               widget=forms.Select(attrs={"class":"form-control"}), required=False)

    session_start = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}), required=False)

    session_end = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}), required=False)

    profile_pic = forms.FileField(label="Image", widget=forms.FileInput(attrs={"class":"form-control"}), required=False)