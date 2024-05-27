from django.shortcuts import render
from django.http import HttpResponse

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

def Register(request):

    return(request, 'login.html')


def Login(request):

    return(request, 'login.html')


