from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, UserProfileInfoForm


# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello from home_page in template", 'insert_new': 'do something'}
    return render(request, 'home_page/front_page.html', context=my_dict)


def loginPage(request):
    return render(request, 'home_page/login.html')

    # return HttpResponse("hello world")


def register(request):
    registered = False

    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            #

            # Update with Hashed password
            user.save()

            profile_form = UserProfileInfoForm(data=request.POST)

            profile = profile_form.save(commit=False)
            profile.user = user

            # check if ID is empty

            profile.save()

            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors, profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request, 'home_page/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})
