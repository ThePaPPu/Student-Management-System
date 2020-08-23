from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render

from student_app.EmailBackEnd import EmailBackEnd


def AdminView(request):
    return render(request, "admin.html")

def LoginView(request):
    return render(request, "login.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        # change
        user = EmailBackEnd.authenticate(request,username=request.POST.get("email"),
                                         password=request.POST.get("password"))
        if user is not None:
            login(request,user)
            return HttpResponse("Email : " + request.POST.get("email") + " Password : " + request.POST.get("password"))
        else:
            # login(request, user)
            return HttpResponse("Invalid Login")

def GetUserDetails(request):
    if request.user is not None:
        return HttpResponse("User : " + request.user.email + " Usertype : " + request.user.user_type)
    else:
        return HttpResponse("Please Login First!")