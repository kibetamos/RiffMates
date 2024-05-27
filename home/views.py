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

def register(request):
    content ={ 
        
        "message": "Amok"
    }
    

    return render (request, 'register.html', content)


def login(request):

    content ={ 
        
        "message": "Amok"
    }


    return render (request, 'login.html',content)


