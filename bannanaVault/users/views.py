from multiprocessing import AuthenticationError

from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from users.forms import SignupForm
from passwords.models import PasswordVault
from passwords.forms import CreatePasswordEntryForm

# Create your views here.

def login_view(request):
    """Login View"""
    form = AuthenticationForm()

    if request.method == "POST":
        ### Look at post data and create account
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('home')
    else:
        return render(request, 'users/authentication/login.html', {'form': form})
        ### set up form and render

    return render(request, 'users/authentication/login.html', {'form': form})

def signup(request):

    signup_form = SignupForm()

    if request.method == "POST":
        signup_form = SignupForm(data=request.POST, files=request.FILES)
        ### Look at post data and create account
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('home') # will redirect to home
    context = {'form': signup_form}
    return render(request, 'users/authentication/signup.html', context)

@login_required(login_url='login')
def home(request):
    vault = request.user.password_vault
    
    if request.method == 'POST':
        form = CreatePasswordEntryForm(data=request.POST)
        if form.is_valid():
            pass_entry = form.save(commit=False)
            pass_entry.vault = request.user.password_vault
            # password = pass_entry.generate_password()
            # pass_entry.hash_password(password)
            pass_entry.save()
            return redirect('home')
    else:
        form = CreatePasswordEntryForm()
    password_entries = vault.password_entry.all()
    return render(request, 'home.html', context={'pass_form': form, 'password_entries': password_entries})

@login_required(login_url='login')
def logout_view(request):
    try:
        logout(request)
        return redirect('login')
    except:
        raise AuthenticationError 