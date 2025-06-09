from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from .forms import SignupForm, LoginForm  # Assuming you'll use these forms

# Static Pages
def credits(request):
    """Credits page view"""
    return render(request, 'credits.html', {"message": "Amok"})

def news(request):
    """News page view"""
    news_items = [
        "RiffMates now has a news page!",
        "RiffMates has its first web page",
    ]
    return render(request, "news.html", {'news': news_items})

# Authentication Views
@csrf_protect
@require_http_methods(["GET", "POST"])
def register(request):
    """User registration view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        terms = request.POST.get('terms')

        # Validation
        if not all([username, email, password1, password2, terms]):
            messages.error(request, 'Please fill out all fields.')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif len(password1) < 8:
            messages.error(request, 'Password must be at least 8 characters.')
        else:
            try:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists.')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already registered.')
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password1
                    )
                    auth_login(request, user)
                    messages.success(request, 'Registration successful!')
                    return redirect('home')
            except Exception as e:
                messages.error(request, f'Registration error: {str(e)}')
    
    return render(request, 'registration/register.html')

@csrf_protect
@require_http_methods(["GET", "POST"])
def login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not (username and password):
            messages.error(request, 'Both username and password are required')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password')

    return render(request, 'registration/login.html')

def user_logout(request):
    """User logout view"""
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
    return redirect('login')