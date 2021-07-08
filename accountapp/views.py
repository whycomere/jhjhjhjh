from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    if request.method == "post":
        return render(request, 'accountapp/hello_world.html', context={'text': 'post method!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'get method!'})


# def hello_world(request):
#     return render(request, 'accountapp/hello_world.html')
