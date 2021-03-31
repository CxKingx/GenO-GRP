from django.urls import path
from home_page import views
from django.conf.urls import url, include

app_name = 'home_page'

# for helping taking actions against user activities

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
]
