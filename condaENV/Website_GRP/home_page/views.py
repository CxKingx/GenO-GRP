from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UserForm, UserProfileInfoForm, VideoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import UserProfileInfo
from .models import Project
# from .models import Project_Artefact_Connector
# from .models import Account_Project_Connector
from .models import Artefact_Info
# from home_page.models import Artefact_Info
from home_page.models import Video_Artefact

from django.contrib.auth import get_user_model
from datetime import datetime, timedelta, date
from django.utils import timezone

User = get_user_model()


# to call user


# Create your views here.
# views for doing activities behind the scenes

def index(request):
    my_dict = {'insert_me': "Hello from home_page in template", 'insert_new': 'do something'}
    return render(request, 'home_page/front_page.html', context=my_dict)


# to help redirect back to login page

def loginPage(request):
    # return render(request, 'home_page/login.html')
    wrongpassword = True
    context = {'wrongpassword': wrongpassword}
    return render(request, 'home_page/StudentLogin.html', context)
    # return HttpResponse("hello world")


def adminLogin(request):
    # return render(request, 'home_page/login.html')
    wrongpassword = True
    context = {'wrongpassword': wrongpassword}
    return render(request, 'home_page/adminLogin.html', context)
    # return HttpResponse("hello world")


def welcomepage(request):
    return render(request, 'home_page/WelcomePage.html', {})


def indexbase(request):
    return render(request, 'home_page/testextention.html', {})


def footertest(request):
    return render(request, 'home_page/footer.html', {})


def layout(request):
    return render(request, 'home_page/layout.html', {})


def studentdashboardcontent(request):
    return render(request, 'home_page/studentdashboardcontent.html', {})


# employees = Employee.objects.all().values('id','name','company__name')
@login_required
def upload_project(request):
    return render(request, 'home_page/ProjectUploadPage.html', {})


@login_required
def edit_project(request):
    if request.method == 'POST':
        ProjectID = request.POST.get('EditProject')
        print("this is project ID after button")
        print(ProjectID)
        print(request.user)
        # Process this project ID


@login_required
def studentdashboard(request):
    thisuser = request.user
    #print(thisuser)

    # Get the current User ID , then get all the projects that belong to this User ID
    getCurrentUser = User.objects.prefetch_related().get(username=thisuser)
    getCurrentUserID = UserProfileInfo.objects.get(user_id=getCurrentUser.id)
    getUserProjects = Project.objects.filter(User_Owner_id=getCurrentUserID.id)
    # Cannot use .get() as it will only return 1 object , and if it tries to take more than 1
    # it will give some error

    # Get today Date to check if user can still edit or not DateField Object
    todayDate = date.today()

    #print(getCurrentUser.id)
    #print(getCurrentUserID.id)
    #print(getUserProjects)
    #print(todayDate)


    # DateTime Object , Is not needed for this type of website
    # todayDate = (timezone.now())
    # Get a dateField Object that is 7days , can be added or substracted to an existing DateField Object
    # nextweek = timedelta(days=7)
    # nextweekDate = todayDate + nextweek

    ProjectExists = False

    # Approval_Date
    if getUserProjects.exists():
        ProjectExists = True
        #print("not empty")
    else:
        ProjectExists = False
        #print("empty")

    #print(ProjectExists)

    context = {'getUserProjects': getUserProjects,
               'ProjectExists': ProjectExists,
               'todayDate': todayDate}
    # return render(request, 'home_page/studentDashboardtest.html', context)
    return render(request, 'home_page/studentdashboardcontent.html', context)

    # return render(request, 'home_page/studentDashboard.html', {})




def error_404(request, exception):
    return render(request, 'home_page/ivanoldlogin.html')


# add other errors

#This special for now is uselss
@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))  # There is a problem here to return logout page


# After logout , redirect using here


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


def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            # Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)
                # Send the user back to homepage.

                return HttpResponseRedirect(reverse('index'))
            #
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            #print("Someone tried to login and failed.")
            #print("They used username: {} and password: {}".format(username, password))
            # I must edit this to redirect back to login
            # return HttpResponse("Invalid login, this needs to redirect back and add a text ,"
            # "right now only back to login but no text invalid login")
            wrongpassword = False
            context = {'wrongpassword': wrongpassword}
            return render(request, 'home_page/StudentLogin.html', context)

    else:
        # Nothing has been provided for username or password.
        return render(request, 'home_page/login.html', {})


def showvideo(request):
    # This 2 commands is searching for a file in the database, so if no video = eror
    # cara ambil hrs beda, hrs pake reference ke user
    lastvideo = Video_Artefact.objects.last()
    videofile = lastvideo.videofile

    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'videofile': videofile,
               'form': form
               }

    return render(request, 'home_page/UploadTest.html', context)


from django.db.models import Q


def searchbar(request):
    if request.method == "GET":
        search = request.GET.get('search')
        # post = Artefact_Info.objects.all().filter(Q(ArtefactName__icontains=search))
        post = Video_Artefact.objects.all().filter(Q(name__icontains=search))
        return render(request, 'home_page/searchbar.html', {'post': post})

# Extra codes for future use

# for admin , view all things
# newobject0 = User.objects.select_related().all()
# newobject1 = UserProfileInfo.objects.select_related().all()
# newobject2 = Project.objects.select_related().all()
# newobject3 = Project_Artefact_Connector.objects.select_related().all()
# newobject4 = Artefact_Info.objects.select_related().all()
# newobject5 = Account_Project_Connector.objects.select_related().all()
# print(newobject0)
# print(newobject1)
# print(newobject2)
# print(newobject3)
# print(newobject4)
# print(newobject5)

# Basics of taking data = models.objects.all()
