from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import message

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_app.EmailBackEnd import EmailBackEnd


def DemoView(request):
    return render(request, "demo.html")

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
            return HttpResponseRedirect('/admin_home')
        else:
            # login(request, user)
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user is not None:
        return HttpResponse("User : " + request.user.email + " Usertype : " + request.user.user_type)
    else:
        return HttpResponse("Please Login First!")

def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")