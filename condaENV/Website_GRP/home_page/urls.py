from django.urls import path
from home_page import views
from django.conf.urls import url, include

app_name = 'home_page'

# for helping taking actions against user activities

urlpatterns = [
    path('', views.index, name='front_page'),
    # path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('edit_project/', views.edit_project, name='edit_project'),

]
