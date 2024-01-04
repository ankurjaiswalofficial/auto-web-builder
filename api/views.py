from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import UserProfile
from .forms import UserProfileForm
import secrets
import string

def generate_api_key():
    alphabet = string.ascii_letters + string.digits
    api_key = ''.join(secrets.choice(alphabet) for _ in range(40))  # Generating a 40-character long key
    return api_key

@login_required
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_setup')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile_setup')  # Redirect to profile completion page after login
    return render(request, 'registration/login.html')

def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Logic to send password reset email
            pass
    else:
        form = PasswordResetForm()
    return render(request, 'registration/forgot_password.html', {'form': form})

@login_required
def profile_setup(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Save user profile details, generate API key, and associate it with the user
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.api_key = generate_api_key()  # Implement a function to generate API key
            user_profile.save()
            return redirect('home')  # Redirect to homepage after profile completion
    else:
        form = UserProfileForm()
    return render(request, 'profile/profile_setup.html', {'form': form})
