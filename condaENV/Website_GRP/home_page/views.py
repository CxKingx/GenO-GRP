from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from home_page.models import Video_Artefact
from .forms import UserForm, UserProfileInfoForm, VideoForm, ImageForm

from home_page.models import Artefact_Info


from .forms import UserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import UserProfileInfo
from .models import Project
#from .models import Project_Artefact_Connector
#from .models import Account_Project_Connector
from .models import Artefact_Info

from django.contrib.auth import get_user_model

User = get_user_model()


# to call user


# Create your views here.
# views for doing activities behind the scenes

def index(request):
    my_dict = {'insert_me': "Hello from home_page in template", 'insert_new': 'do something'}
    return render(request, 'home_page/front_page.html', context=my_dict)


# to help redirect back to login page

def loginPage(request):
    return render(request, 'home_page/login.html')

    # return HttpResponse("hello world")


def welcomepage(request):
    return render(request, 'home_page/WelcomePage.html', {})


def indexbase(request):
    return render(request, 'home_page/testextention.html', {})


def footertest(request):
    return render(request, 'home_page/footer.html', {})


# employees = Employee.objects.all().values('id','name','company__name')
@login_required
def studentdashboard(request):

    thisuser = request.user
    print(thisuser)
    # print(thisuser.Project_Name)
    print("List of QUeries")
    newobject0 = User.objects.select_related().all()
    newobject1 = UserProfileInfo.objects.select_related().all()
    newobject2 = Project.objects.select_related().all()
    #newobject3 = Project_Artefact_Connector.objects.select_related().all()
    newobject4 = Artefact_Info.objects.select_related().all()
    #newobject5 = Account_Project_Connector.objects.select_related().all()
    print(newobject0)
    print(newobject1)
    print(newobject2)
    #print(newobject3)
    print(newobject4)
    #print(newobject5)
    print("allo")

    #print(newobject2[0].Project_Name + " ,"+newobject2[0].Project_Description )

    thismodel = UserProfileInfo.objects.select_related().all()
    #thismodel2 = UserProfileInfo.objects.get(user='thisuser')
    print(thismodel)

    anothermodel = User.objects.all()
    print(anothermodel)

    print("Model3")
    thismodel3 = User.objects.get(username=thisuser)
    print(thismodel3)
    print(thismodel3.email)

    #get all from user ,
    print("Model4")
    thismodel4 = User.objects.select_related().get(username=thisuser)
    print(thismodel4)
    #print(thismodel4.Project_Name)

    #print("Model5")
    #thismodel5 = Artefact_Info.objects.select_related('Project_Owner').get(ArtefactName = 'CxKingx no video')
    #print(thismodel5 )
    #print(thismodel5)
    #print(thismodel5.Project_Owner)
    #print(thismodel5.ArtefactName)

    print("Model6")
    thismodel6 = UserProfileInfo.objects.select_related('user').all()
    print(thismodel6)

    print("Model7")
    thismodel7 = Project.objects.all()
    print(thismodel7)
    #print(thismodel7[0].Project_Name)
    # for i in thismodel7:
    #     {
    #         i.
    #     }
    #print("Model8")
    #thismodel8 = Project.objects.select_related('User_Owner').get(User_Owner='20182120')
    #print(thismodel8)

    #most important 9 10 12

    print("Model9")
    thismodel9 = User.objects.prefetch_related().get(username=thisuser)
    print(thismodel9)
    print(thismodel9.id)

    print("Model10")
    thismodel10 = UserProfileInfo.objects.get(user_id=thismodel9.id)
    print(thismodel10)
    print(thismodel10.StudentID)
    print(thismodel10.id)

    #if get more than 2 erorr
    #print("Model11")
    #thismodel11 = Project.objects.get(User_Owner_id=thismodel10.id).all()
    #print(thismodel11)
    #print(newobject2.User_Owner_id)
    #filter?

    print("Model12")
    thismodel12 = Project.objects.filter(User_Owner_id=thismodel10.id)
    print(thismodel12)
    print(type(thismodel12[0].Project_Approval_Status))

    if thismodel12.exists():
        print("not empty")
    else:
        print("empty")
    #print(thismodel12[0].Project_Name)
    #print(thismodel12[0].Project_Description)
    #print(thismodel12[1].Project_Name)
    #print(thismodel12[1].Project_Description)
    #print(thismodel12[0].Project_Approval_Status)
    #print(type(thismodel12[0].Project_Approval_Status))
    #Projects.object.get(id = thismodel9.id )

    #User_Owner
    #Project_Name
    #prefetch_related
    #cri model user, ke student profile info ,
    #from user , get all project that is related from user , in a list right? , so now from 0 - project , get the artefacts that is related to it

    # select_related = ("user", "group")
    #print("Model4")
    #thismodel4 = Project.objects.get(Project_Name='Project1')
    #print(thismodel4)
    #print("Model5")
    #thismodel5 = thismodel4.User_Owner
    #print(thismodel5)
    # thisuser2 = UserProfileInfo.objects.select_related('').all()
    # print(thisuser)

    context = {'thismodel12': thismodel12}
    return render(request, 'home_page/studentDashboard.html', context)
    #return render(request, 'home_page/studentDashboard.html', {})

# return render(request, 'home_page/login.html')


def error_404(request, exception):
    return render(request, 'home_page/ivanoldlogin.html')


# add other errors

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
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            #
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            # I must edit this to redirect back to login
            return HttpResponse("Invalid login, this needs to redirect back and add a text ,"
                                "right now only back to login but no text invalid login")
            # return render(request, 'home_page/login.html', {})

    else:
        # Nothing has been provided for username or password.
        return render(request, 'home_page/login.html', {})


def showvideo(request):
    #This 2 commands is searching for a file in the database, so if no video = eror
    #cara ambil hrs beda, hrs pake reference ke user
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
        #post = Artefact_Info.objects.all().filter(Q(ArtefactName__icontains=search))
        post = Video_Artefact.objects.all().filter(Q(name__icontains=search))
        return render(request, 'home_page/searchbar.html', {'post': post})


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'home_page/uploadimage.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()

    return render(request, 'home_page/uploadimage.html', {'form': form})



# Extra codes for future use

# for admin , view all things
    #newobject0 = User.objects.select_related().all()
    #newobject1 = UserProfileInfo.objects.select_related().all()
    #newobject2 = Project.objects.select_related().all()
    #newobject3 = Project_Artefact_Connector.objects.select_related().all()
    #newobject4 = Artefact_Info.objects.select_related().all()
    #newobject5 = Account_Project_Connector.objects.select_related().all()
    #print(newobject0)
    #print(newobject1)
    #print(newobject2)
    #print(newobject3)
    #print(newobject4)
    #print(newobject5)

    #Basics of taking data = models.objects.all()