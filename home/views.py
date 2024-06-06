from importlib.resources import contents
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth import authenticate, login as auth_login
from .forms import SignupForm, LoginForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


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
    # username
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    

    return render (request, 'register.html',{'form': form})


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