"""Website_GRP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home_page import views
from django.conf.urls import include

# naming convention , all is small letters , spaces use _ , so ex like hello_world
# this is the base redirection

urlpatterns = [
    # Add paths here to add new pages -Ivan
    path('', views.welcomepage, name='index'),
    # path('Login/', views.loginPage, name='loginPage'),

    path('Login/', views.loginPage, name='loginPage'),
    path('register/', views.register, name='register'),
    path('website_base/', include('home_page.urls')),  # website_base/ is the name of the extension can be anything.
    # to help
    path('admin/', admin.site.urls),
    path('logout/', views.user_logout, name='logout'),
    path('welcome/', views.welcomepage, name='welcomepage'),


    path('footertest/', views.footertest, name='footertest'),
    path('indexbase/', views.indexbase, name='indexbase'),

]
