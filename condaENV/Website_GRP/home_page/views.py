from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello from home_page in template"}
    return render(request, 'home_page/index.html', context=my_dict)


    #return HttpResponse("hello world")
