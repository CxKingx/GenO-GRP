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

from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views

# naming convention , all is small letters , spaces use _ , so ex like hello_world
# this is the base redirection

urlpatterns = [
    # Add paths here to add new pages -Ivan
    path('', views.welcomepage, name='index'),
    # Final
    path('admin/', admin.site.urls),
    path('Login/', views.loginPage, name='loginPage'),
    path('logout/', views.user_logout, name='logout'),
    path('website_base/', include('home_page.urls')),  # website_base/ is the name of the extension can be anything.

    #Still needs to be edited
    path('register/', views.register, name='register'),

    path('upload_project/', views.upload_project, name='upload_project'),

    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),


    path('welcome/', views.welcomepage, name='welcomepage'),
    path('upload_artefact/', views.showvideo, name = 'showvideo'),

    path('studentdashboard/', views.studentdashboard, name='studentdashboard'),

    path('layout/', views.layout, name='layout'),
    path('studentdashboardcontent/', views.studentdashboardcontent, name='studentdashboardcontent'),

    path('uploadimage/', views.image_upload_view, name = 'upload_image_view'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('footertest/', views.footertest, name='footertest'),
    path('indexbase/', views.indexbase, name='indexbase'),

    # path('studentdashboard/studentdashboardredirect', views.studentdashboardredirect, name='studentdashboardredirect'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

# https://www.digitalocean.com/community/tutorials/how-to-troubleshoot-common-http-error-codes

handler404 = 'home_page.views.error_404'
handler400 = 'home_page.views.error_404'
handler403 = 'home_page.views.error_404'
# handler500 = 'home_page.views.error_404'

