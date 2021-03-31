from django.urls import path
from home_page import views
from django.conf.urls import url, include

app_name = 'home_page'

# Django urls help to ease referencing to pages or other views , so it will not be hardcoded
# it helps redirect users to certain locations or in templates to provide enough user navigation.

# These urls are helpers to the main urls , as an extension

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
]
