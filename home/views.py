from importlib.resources import contents
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth import authenticate, login as auth_login
from .forms import SignupForm, LoginForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def credits(request):
    content ={ 
        
        "message": "Amok"
    }
    return render(request,'credits.html', content)


def news(request):
    data={
        'news':[
            "RiffMates now has a news page!",
            "RiffMates has its first web page",
            # 'book':{
            #     'name':'Damu nNyeusi'
            # }
        ],
    }

    return render(request, "news.html", data)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        country = request.POST.get('country')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        terms = request.POST.get('terms')

        if not all([username, email, country, password1, password2, terms]):
            messages.error(request, 'Please fill out all fields.')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match.')
        else:
            try:
                user = User.objects.create(
                    username=username,
                    email=email,
                    password=make_password(password1)
                )
                # Here you can also save the country information to the user's profile if you have one
                auth_login(request, user)
                messages.success(request, 'Registration successful')
                return redirect('home')
            except Exception as e:
                messages.error(request, f'Error: {e}')
    return render (request, 'register.html')


def login(request):

    if request.method == 'POST':

        username = request.POST.get('username', '')

        password = request.POST.get('password', '')

        if username and password:

            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                auth_login(request, user)

                return redirect('home')  # Redirect to the home page or another page
            else:

                messages.error(request, 'Invalid username or password')

        else:

            messages.error(request, 'Both username and password are required')

    return render(request, 'login.html')


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')