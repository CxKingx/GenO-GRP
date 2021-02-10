from django.urls import path
from home_page import views

app_name = 'home_page'

urlpatterns = [
    path('', views.index, name='front_page'),
    #path('register/', views.register, name='register'),

]
