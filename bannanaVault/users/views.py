from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# from bannanaVault.bannanaVault.users import forms
from users.forms import SignupForm
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    """Login View"""
    form = AuthenticationForm()

    if request.method == "POST":
        ### Look at post data and create account
        form =  AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('home')
    else:
        return render(request, 'login.html', {'form': form},)
        ### set up form and render

    return render(request, 'users/authentication/login.html')

def signup(request):

    signup_form = SignupForm()

    if request.method == "POST":
        signup_form = SignupForm(request.POST, request.FILES)
        ### Look at post data and create account
        if signup_form.is_valid():
            user = signup_form.save()
            if authenticate(username=user.username, password=user.password):
                login(request, user)
                return redirect('home') # will redirect to home
            raise forms.ValidationError('Something went wrong.')
    context = {'form': signup_form}
    return render(request, 'users/authentication/signup.html', context)

@login_required
def home(request):
    return render(request, 'home.html')