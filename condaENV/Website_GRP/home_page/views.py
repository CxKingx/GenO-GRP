from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello from home_page in template", 'insert_new' : 'do something'}
    return render(request, 'home_page/front_page.html', context=my_dict)

def loginPage(request):
    return render(request, 'home_page/login.html')


    #return HttpResponse("hello world")
