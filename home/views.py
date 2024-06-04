from importlib.resources import contents
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm

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

        form = LoginForm(request.POST)

        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()

    return render (request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')