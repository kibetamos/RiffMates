from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def credits(request):
    content = "Amok"

    return HttpResponse(content, content_type="text/plain")


def news(request):
    data={
        'news':[
            "RiffMates now has a news page!",
            "RiffMates has its first web page",
        ],
    }

    return render(request, "news.html", data)