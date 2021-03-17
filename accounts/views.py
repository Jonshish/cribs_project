from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are now registerd and can login')
            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')