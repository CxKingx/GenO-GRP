from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from home_page.models import VideoArtefact
from .forms import UserForm, UserProfileInfoForm, VideoForm, ImageForm, ProjectForm, UploadImageForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import UserProfileInfo
from .models import Project
from .models import ImageArtefact
# from home_page.models import Artefact_Info
from home_page.models import VideoArtefact

from django.contrib.auth import get_user_model
from datetime import datetime, timedelta, date
from django.utils import timezone

from django.db.models import Q

# to call user
User = get_user_model()


# Create your views here.
# views for doing activities behind the scenes

# Return the first page for index
def index(request):
    my_dict = {'insert_me': "Hello from home_page in template", 'insert_new': 'do something'}
    return render(request, 'home_page/front_page.html', context=my_dict)


# Takes User to Student Login Page
def loginPage(request):
    wrongpassword = True
    context = {'wrongpassword': wrongpassword}
    return render(request, 'home_page/StudentLogin.html', context)
    # return HttpResponse("hello world")


# Takes User to Admin Login Page
def adminLogin(request):
    # return render(request, 'home_page/login.html')
    wrongpassword = True
    context = {'wrongpassword': wrongpassword}
    return render(request, 'home_page/adminLogin.html', context)
    # return HttpResponse("hello world")


def welcomepage(request):
    return render(request, 'home_page/WelcomePage.html', {})


def oldregister(request):
    user_form = UserForm()
    profile_form = UserProfileInfoForm()
    # print(formcorrect)
    # This is the render and context dictionary to feed
    # back to the registration.html file page.

    # return render(request, 'home_page/register.html',

    return render(request, 'home_page/accountRegistrationold.html',
                  {'user_form': user_form,
                   'profile_form': profile_form, })


# Test Return Pages


def indexbase(request):
    return render(request, 'home_page/testextention.html', {})


def footertest(request):
    return render(request, 'home_page/footer.html', {})


def layout(request):
    return render(request, 'home_page/layout.html', {})


def secondaryLayout(request):
    return render(request, 'home_page/secondaryLayout.html', {})


def studentdashboardcontent(request):
    return render(request, 'home_page/studentdashboardcontent.html', {})


def contactUs(request):
    return render(request, 'home_page/contactUs.html', {})


# End of Test Return Pages

# employees = Employee.objects.all().values('id','name','company__name')
# Project Upload Page does not use Secondary Layout because it crashes
@login_required
def ProjectUploadPage(request):
    if request.method == 'POST':
        Projectformhtml = ProjectForm(request.POST, request.FILES)
        # form = VideoForm(request.POST or None, request.FILES or None)

        # imageform = UploadImageForm(request.POST or None, request.FILES or None)
        if Projectformhtml.is_valid():
            thisuser = request.user
            getCurrentUser = User.objects.prefetch_related().get(username=thisuser)

            getCurrentUserID = UserProfileInfo.objects.get(user_id=getCurrentUser.id)
            print(getCurrentUser.email)
            print(type(getCurrentUserID))

            uploadedProject = Projectformhtml.save(commit=False)
            uploadedProject.Upload_Date = date.today()
            uploadedProject.Last_Updated = date.today()
            todayDate = date.today()
            nextweek = timedelta(days=7)
            nextweekDate = todayDate + nextweek
            uploadedProject.Account_ExpiryDate = nextweekDate
            print(request.user)
            print(getCurrentUserID.user)
            uploadedProject.User_Owner = getCurrentUserID
            uploadedProject.save()

            print(uploadedProject)
            print(type(uploadedProject))

            # print("Handle videos")
            # thisvideo = form.save(commit=False)
            # thisvideo.Project_Name = uploadedProject
            # thisvideo.save()
            # print("Saved")
            #
            # imageattribute = imageform.save(commit=False)
            # imageattribute.Project_Name = uploadedProject
            # imageattribute.save()

            return render(request, 'home_page/ProjectUploadPage.html')
        else:
            print(Projectformhtml.errors.as_data())
            return render(request, 'home_page/ProjectUploadPage.html')

    else:
        Projectformhtml = ProjectForm()
        # form = VideoForm()
        # imageform = UploadImageForm()
    return render(request, 'home_page/ProjectUploadPage.html', {'Projectformhtml': Projectformhtml})
    # return render(request, 'home_page/ProjectUploadPage.html', {})


@login_required
def edit_project(request):
    if request.method == 'POST':
        ProjectID = request.POST.get('EditProject')
        print("this is project ID after button")
        print(ProjectID)
        print(request.user)
        print(type(ProjectID))
        # Process this project ID


@login_required
def studentdashboard(request):
    thisuser = request.user
    # print(thisuser)

    # Get the current User ID , then get all the projects that belong to this User ID
    getCurrentUser = User.objects.prefetch_related().get(username=thisuser)
    getCurrentUserID = UserProfileInfo.objects.get(user_id=getCurrentUser.id)
    getUserProjects = Project.objects.filter(User_Owner_id=getCurrentUserID.id)
    # Cannot use .get() as it will only return 1 object , and if it tries to take more than 1
    # it will give some error

    # Get today Date to check if user can still edit or not DateField Object
    todayDate = date.today()

    # print(getCurrentUser.id)
    # print(getCurrentUserID.id)
    # print(getUserProjects)
    # print(todayDate)

    # DateTime Object , Is not needed for this type of website
    # todayDate = (timezone.now())
    # Get a dateField Object that is 7days , can be added or substracted to an existing DateField Object
    # nextweek = timedelta(days=7)
    # nextweekDate = todayDate + nextweek

    ProjectExists = False

    # Approval_Date
    if getUserProjects.exists():
        ProjectExists = True
        # print("not empty")
    else:
        ProjectExists = False
        # print("empty")

    # print(ProjectExists)

    context = {'getUserProjects': getUserProjects,
               'ProjectExists': ProjectExists,
               'todayDate': todayDate}
    # return render(request, 'home_page/studentDashboardtest.html', context)
    return render(request, 'home_page/studentdashboardcontent.html', context)

    # return render(request, 'home_page/studentDashboard.html', {})


def error_404(request, exception):
    return render(request, 'home_page/ivanoldlogin.html')


# add other errors

# This special for now is uselss
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
    if request.user.is_staff and request.user.is_superuser:
        print("Staff has logined")
    else:
        return render(request, 'home_page/adminLogin.html')

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

            # Update with Hashed password
            user.save()

            profile_form = UserProfileInfoForm(data=request.POST)

            profile = profile_form.save(commit=False)

            profile.user = user

            # check if ID is empty

            profile.save()

            registered = True
            print("registered")

            # return render(request, 'home_page/accountRegistration.html', {'registered': registered})
            return render(request, 'home_page/registerSuccess.html', {'registered': registered})

        else:
            # One of the forms was invalid if this else gets called.
            # print(user_form.errors, profile_form.errors)
            print(user_form.errors.as_data(), profile_form.errors.as_data())
            # return render(request, 'home_page/register.html',

            return render(request, 'home_page/accountRegistration.html',
                          {'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.

    # return render(request, 'home_page/register.html',
    return render(request, 'home_page/accountRegistration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})
    # 'formcorrect': formcorrect})


# accountRegistration

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

                return HttpResponseRedirect(reverse('studentdashboard'))
            #
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            # print("Someone tried to login and failed.")
            # print("They used username: {} and password: {}".format(username, password))
            # I must edit this to redirect back to login
            # return HttpResponse("Invalid login, this needs to redirect back and add a text ,"
            # "right now only back to login but no text invalid login")
            wrongpassword = False
            context = {'wrongpassword': wrongpassword}
            return render(request, 'home_page/StudentLogin.html', context)

    else:
        # Nothing has been provided for username or password.
        return render(request, 'home_page/login.html', {})


def admin_login(request):
    print("admin login")
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
                if user.is_superuser:
                    print("Superuser")
                    login(request, user)
                    # Send the user back to homepage.

                    return HttpResponseRedirect(reverse('register'))
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not superuser.")
            #
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            # print("Someone tried to login and failed.")
            # print("They used username: {} and password: {}".format(username, password))
            # I must edit this to redirect back to login
            # return HttpResponse("Invalid login, this needs to redirect back and add a text ,"
            # "right now only back to login but no text invalid login")
            wrongpassword = False
            context = {'wrongpassword': wrongpassword}
            return render(request, 'home_page/accountRegistration.html', context)

    else:
        # Nothing has been provided for username or password.
        return render(request, 'home_page/admin_login.html', {})


def showvideo(request):
    # This 2 commands is searching for a file in the database, so if no video = eror
    # cara ambil hrs beda, hrs pake reference ke user
    lastvideo = VideoArtefact.objects.last()
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
        getCurrentUser = User.objects.prefetch_related().filter(Q(username__icontains=search))
        if (getCurrentUser.exists()):
            getCurrentUser = User.objects.prefetch_related().get(username=search)
            getCurrentUserID = UserProfileInfo.objects.get(user_id=getCurrentUser.id)
            post = Project.objects.filter(User_Owner_id=getCurrentUserID.id)

        else:
            ProjectFile = VideoArtefact.objects.all().filter(Project_Owner__iexact=1)
            print(ProjectFile)
            post = Project.objects.all().filter(Q(Project_Name__icontains=search) | Q(Project_Tag__icontains=search))
        return render(request, 'home_page/searchbar.html', {'post': post}, {'ProjectFile': ProjectFile})

        # Project query works, now just need to query video/image artefact to show with the rest.
        # maybe use context = { asdasdadasda } to send all data at once.


# The test version
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


def testuploadproject(request):
    # Projectformhtml = ProjectForm()
    if request.method == 'POST':
        Projectformhtml = ProjectForm(request.POST, request.FILES)
        # form = VideoForm(request.POST or None, request.FILES or None)

        # imageform = UploadImageForm(request.POST or None, request.FILES or None)
        if Projectformhtml.is_valid():
            thisuser = request.user
            getCurrentUser = User.objects.prefetch_related().get(username=thisuser)

            getCurrentUserID = UserProfileInfo.objects.get(user_id=getCurrentUser.id)
            print(getCurrentUser.email)
            print(type(getCurrentUserID))

            uploadedProject = Projectformhtml.save(commit=False)
            print("Wat if nto saved yet")
            print(uploadedProject.id)
            uploadedProject.Upload_Date = date.today()
            uploadedProject.Last_Updated = date.today()
            todayDate = date.today()
            nextweek = timedelta(days=7)
            nextweekDate = todayDate + nextweek
            uploadedProject.Account_ExpiryDate = nextweekDate
            print(thisuser)
            print(getCurrentUserID.user)
            uploadedProject.User_Owner = getCurrentUserID
            uploadedProject.save()
            print(uploadedProject)
            print(type(uploadedProject))

            # print("Handle videos")
            # thisvideo = form.save(commit=False)
            # thisvideo.Project_Name = uploadedProject
            # thisvideo.save()
            # print("Saved")
            #
            # imageattribute = imageform.save(commit=False)
            # imageattribute.Project_Name = uploadedProject
            # imageattribute.save()

            print("Pass dis")
            print(uploadedProject.id)
            print(uploadedProject)
            request.session['thisdata'] = uploadedProject.id
            bruh = request.session['thisdata']
            print(bruh)
            print("Project Uploaded, now go to summary")
            return HttpResponseRedirect(reverse('testProjectSummary'))
        # return render(request, 'home_page/testProjectSummary.html')


    else:
        Projectformhtml = ProjectForm()
        form = VideoForm()
        imageform = UploadImageForm()
    return render(request, 'home_page/testuploadproject.html', {'Projectformhtml': Projectformhtml, 'form': form,
                                                                'imageform': imageform})


# Project form save first
# Then save picture form and video form , connect them to project

def testProjectVideo(request):
    bruh = request.session['thisdata']
    print(bruh)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():

            uploadedVideo = form.save(commit=False)
            CurrentProject = Project.objects.get(id=request.session['thisdata'])
            uploadedVideo.Project_Name = CurrentProject
            uploadedVideo = form.save()
            print("hai")
            return HttpResponseRedirect(reverse('testProjectSummary'))
        else:
            print("Not valid")
            print(form.errors.as_data())
            # return render(request, 'home_page/register.html',

            return render(request, 'home_page/testProjectVideo.html', {'Projectformhtml': Projectformhtml, 'form': form,
                                                                       'imageform': imageform})

    else:
        Projectformhtml = ProjectForm()
        form = VideoForm()
        imageform = UploadImageForm()
        return render(request, 'home_page/testProjectVideo.html', {'Projectformhtml': Projectformhtml, 'form': form,
                                                                   'imageform': imageform})


def testProjectImage(request):
    bruh = request.session['thisdata']
    print(bruh)
    if request.method == 'POST':
        imageform = UploadImageForm(request.POST, request.FILES)
        if imageform.is_valid():

            uploadedImage = imageform.save(commit=False)
            CurrentProject = Project.objects.get(id=request.session['thisdata'])
            uploadedImage.Project_Name = CurrentProject
            uploadedImage = imageform.save()
            print("zzz")
            return HttpResponseRedirect(reverse('testProjectSummary'))
        else:

            print("Failed")
            return HttpResponseRedirect(reverse('testProjectSummary'))
    else:
        Projectformhtml = ProjectForm()
        form = VideoForm()
        imageform = UploadImageForm()
        return render(request, 'home_page/testProjectImage.html', {'Projectformhtml': Projectformhtml, 'form': form,
                                                                   'imageform': imageform})


def testProjectSummary(request):
    print("Showing summary")
    print(request.session['thisdata'])
    CurrentProject = Project.objects.get(id=request.session['thisdata'])
    ProjectImages = ImageArtefact.objects.filter(Project_Name=CurrentProject)
    ProjectVideos = VideoArtefact.objects.filter(Project_Name=CurrentProject)
    print(CurrentProject)
    print(CurrentProject.Project_Name)
    Projectformhtml = ProjectForm()
    form = VideoForm()
    imageform = UploadImageForm()
    print("Deleted BBUTTON")
    if request.method == 'POST':
        ProjectID = request.POST.get('Delete')
        print(ProjectID)
        print(type(ProjectID))
        newint = int(ProjectID)
        print(type(newint))
        ImageWillDelete = VideoArtefact.objects.get(id=newint)
        print(ImageWillDelete.name)
        ImageWillDelete.delete()
    return render(request, 'home_page/testProjectSummary.html', {'Projectformhtml': Projectformhtml, 'form': form,
                                                                 'imageform': imageform,
                                                                 'CurrentProject': CurrentProject
                                        ,'ProjectImages': ProjectImages, 'ProjectVideos': ProjectVideos})


def testProjectDetailEdit(request):
    print("Edit detail")
    print(request.session['thisdata'])
    CurrentProject = Project.objects.get(id=request.session['thisdata'])
    print(CurrentProject)

    if request.method == 'POST':
        Projectformhtml = ProjectForm(request.POST)
        if Projectformhtml.is_valid():
            EditedProject = Projectformhtml.save(commit=False)
            CurrentProject.Project_Name = EditedProject.Project_Name
            CurrentProject.Project_Description = EditedProject.Project_Description
            CurrentProject.Project_Tag = EditedProject.Project_Tag
            CurrentProject.Module_Name = EditedProject.Module_Name
            CurrentProject.Date_of_Completion = EditedProject.Date_of_Completion
            CurrentProject.Author_Comment = EditedProject.Author_Comment
            CurrentProject.Authors = EditedProject.Authors
            CurrentProject.Module_Name = EditedProject.Module_Name
            CurrentProject.save()
            print("Changed")
            #print(EditedProject)
        return HttpResponseRedirect(reverse('testProjectSummary'))
    else:
        Projectformhtml = ProjectForm()
        print("No Changed")
    return render(request, 'home_page/testProjectDetailEdit.html', {'Projectformhtml': Projectformhtml,'CurrentProject': CurrentProject})
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             img_obj = form.instance
#             return render(request, 'home_page/testuploadproject.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#
#     return render(request, 'home_page/uploadimage.html', {'form': form})

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
