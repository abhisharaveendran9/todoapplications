from django.shortcuts import render,redirect
from django.views.generic import View
from todoapp import forms
from django.contrib.auth.models import User

# Create your views here.
class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form=forms.RegistrationForm()
        return render(request,"registration.html",{"form":form})

    def post(self,request,*args,**kwargs):
        # print(request.POST.get("firstname"))
        # print(request.POST.get("lastname"))

        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            #form.save()
            User.objects.create_user(**form.cleaned_data)
            #print("saved")
            return redirect("signin")

        return render(request,"registration.html")


class LoginView(View):

    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        print(request.POST.get("username"))
        print(request.POST.get("password"))
        return render(request,"login.html")