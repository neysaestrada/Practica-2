from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]

        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, "El usuario ya existe")
            else:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                return redirect("home")  # cambia a tu vista principal
        else:
            messages.error(request, "Las contraseñas no coinciden")

    return render(request, "accounts/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

def home_view(request):
    return render(request, "accounts/home.html")
