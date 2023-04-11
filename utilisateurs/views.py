from django.shortcuts import render , redirect
from .forms import LoginForm , RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login

# Create your views here.

def LoginView(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username , password = password)

        if user is not None : 
            login(request , user)
            return redirect("/contacts")

    return render(request , 'Pages/login.html' , {"form" : form})


def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")

            user = authenticate(username=username , password=raw_password)
            return  redirect("/login/")
    else:
        form = RegisterForm()

    return render(request , 'Pages/register.html' , {"form" : form})



