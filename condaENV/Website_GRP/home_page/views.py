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

from home_page.models import VideoArtefact

from django.contrib.auth import get_user_model
from datetime import datetime, timedelta, date
from django.utils import timezone

from django.db.models import Q
from django.core.paginator import Paginator

# to call user model to be used later
User = get_user_model()


# Create your views here.
# views for doing activities behind the scenes

# Return the first page for index

def landingPage(request):
    context = ImageArtefact.objects.all().order_by('Project_Owner__Upload_Date')[:13]
    #13 cards
    return render(request, 'home_page/landingPage.html',{"context":context})

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


def oldregister(request):
    user_form = UserForm()
    profile_form = UserProfileInfoForm()
    # print(formcorrect)
    # This is the render and context dictionary to feed
    # back to the registration.html file page.

    # return render(request, 'home_page/register.html',

    return render(request, 'home_page/accountRegistrationold.html',
              {'user_form': user_form,
               'profile_form': profile_form,})


# Test Return Pages


def indexbase(request):
    return render(request, 'home_page/testextention.html', {})


def footertest(request):
    return render(request, 'home_page/footer.html', {})


def layout(request):
    return render(request, 'home_page/layout.html', {})


def secondaryLayout(request):
    return render(request, 'home_page/secondaryLayout.html', {})


def contactUs(request):
    return render(request, 'home_page/contactUs.html', {})


def showUploadProject(request):
    return render(request, 'home_page/projectUpload.html', {})


def showProjectSummary(request):
    return render(request, 'home_page/projectSummary.html', {})


def showProjectEdit(request):
    return render(request, 'home_page/projectEdit.html', {})


def showProjectUploadImage(request):
    return render(request, 'home_page/uploadImage.html', {})


def showProjectUploadVideo(request):
    return render(request, 'home_page/uploadVideo.html', {})


# End of Test Return Pages

# employees = Employee.objects.all().values('id','name','company__name')
# Project Upload Page does not use Secondary Layout because it crashes
@login_required
def ProjectUpload(request):
    if request.method == 'POST':
        # Get Data from User to be inserted to the object
        Projectformhtml = ProjectForm(request.POST, request.FILES)
        # form = VideoForm(request.POST or None, request.FILES or None)
        # imageform = UploadImageForm(request.POST or None, request.FILES or None)

        if Projectformhtml.is_valid():
            thisuser = request.user
            getCurrentUser = User.objects.prefetch_related().get(username=thisuser)
            getCurrentUserID = UserProfileInfo.objects.get(user_id=getCurrentUser.id)

            # Save the instance first , but not save to the database
            uploadedProject = Projectformhtml.save(commit=False)
            # Add some extra information that is automated by the system
            uploadedProject.Upload_Date = date.today()
            uploadedProject.Last_Updated = date.today()
            todayDate = date.today()
            nextweek = timedelta(days=7)
            nextweekDate = todayDate + nextweek
            uploadedProject.Account_ExpiryDate = nextweekDate

            # print(request.user)
            # print(getCurrentUserID.user)
            # Reference the project to the user uploading it now and Save it
            uploadedProject.User_Owner = getCurrentUserID
            uploadedProject.save()
            # print("This Current Project ID is")
            request.session['thisdata'] = uploadedProject.id
            # print(request.session['thisdata'])
            # return render(request, 'home_page/projectSummary.html')
            return HttpResponseRedirect(reverse('projectSummary'))

        else:
            errormessage = "Something Went Wrong when Uploading / You did not Upload any files"
            errorMessage = True
            print(Projectformhtml.errors.as_data())
            return render(request, 'home_page/projectUploadContent.html', {'errorMessage': errorMessage})

    else:
        # Pass on the empty form as a normal request
        Projectformhtml = ProjectForm()
    return render(request, 'home_page/projectUploadContent.html', {'Projectformhtml': Projectformhtml})
    # return render(request, 'home_page/ProjectUploadPage.html', {})


@login_required
def projectSummary(request):
    print("Showing summary")
    print(request.session['thisdata'])
    CurrentProject = Project.objects.get(id=request.session['thisdata'])
    ProjectImages = ImageArtefact.objects.filter(Project_Owner=CurrentProject)
    ProjectVideos = VideoArtefact.objects.filter(Project_Owner=CurrentProject)

    return render(request, 'home_page/projectSummaryContent.html',
                  {'CurrentProject': CurrentProject, 'ProjectImages': ProjectImages, 'ProjectVideos': ProjectVideos})


# Edit the Details of the Project 'Name , Description , Authors, Date .....
@login_required
def editProjectDetail(request):
    print("Edit Project detail")
    # print(request.session['thisdata'])
    # Get current project being edited
    CurrentProject = Project.objects.get(id=request.session['thisdata'])
    print(CurrentProject)

    if request.method == 'POST':
        Projectformhtml = ProjectForm(request.POST)
        if Projectformhtml.is_valid():
            # Change every attribute of the current project detail into the new one
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
            print("Project Detail Changed , now redirect back to summary")
            # Return it back to Summary
            return HttpResponseRedirect(reverse('projectSummary'))
        else:
            errormessage = "Something Went Wrong when Uploading / You did not Upload any files"
            errorMessage = True
            return render(request, 'home_page/projectEditContent.html',
                          {'errorMessage': errorMessage})
    else:
        Projectformhtml = ProjectForm()
        print("Load the Form with inputs already inserted")
    return render(request, 'home_page/projectEditContent.html',
                  {'Projectformhtml': Projectformhtml, 'CurrentProject': CurrentProject})



# User wants to edit the project, so it will take the Project ID , and display it in the ProjectSummary Page
# Edit from studentdashboard
@login_required
def EditProject(request):
    print("Editing Project")
    ProjectID = request.GET.get('ProjectTag')
    # Set the session to edit the Project with the ID
    request.session['thisdata'] = int(ProjectID)

    # Display it in the Project Summary page
    return HttpResponseRedirect(reverse('projectSummary'))


@login_required
def ProjectUploadImage(request):
    print("Uploading image")
    # bruh = request.session['thisdata']
    CurrentProject = Project.objects.get(id=request.session['thisdata'])

    if request.method == "POST":
        imageform = UploadImageForm(request.POST, request.FILES)
        if imageform.is_valid():
            uploadedImage = imageform.save(commit=False)
            uploadedImage.Project_Owner = CurrentProject
            # uploadedImage = imageform.save()
            uploadedImage.save()
            print("Image Saved")
            # Return it back to Summary
            return HttpResponseRedirect(reverse('projectSummary'))
        else:
            print("Failed to Upload")
            errormessage = "Something Went Wrong when Uploading / You did not Upload any files"
            errorMessage = True
            return render(request, 'home_page/uploadImageContent.html', {'errorMessage': errorMessage})

    else:
        imageform = UploadImageForm()
        print("Load this as a form for uploading image")
        return render(request, 'home_page/uploadImageContent.html')


@login_required
def ProjectUploadVideo(request):
    # Get the project being edited from The Session Data
    print("Uploading Video")
    # request.session['thisdata']
    CurrentProject = Project.objects.get(id=request.session['thisdata'])
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)

        if form.is_valid():
            uploadedVideo = form.save(commit=False)
            uploadedVideo.Project_Owner = CurrentProject
            # uploadedVideo = form.save()
            uploadedVideo.save()
            print("Video is Saved")
            # Return it back to Summary
            return HttpResponseRedirect(reverse('projectSummary'))
        else:
            print("Not valid")
            print(form.errors.as_data())
            errormessage = "Something Went Wrong when Uploading / You did not Upload any files"
            errorMessage = True
            # return render(request, 'home_page/uploadVideoContent.html')
            return render(request, 'home_page/uploadVideoContent.html', {'errorMessage': errorMessage})
    else:
        print("Failed to Upload")
        form = VideoForm()
    return render(request, 'home_page/uploadVideoContent.html', {'form': form})
    # return render(request, 'home_page/uploadVideoContent.html',{'form': form})


@login_required
def deleteImage(request):
    print("Deleting Image")
    # Get the Current Image ID and Delete the Image
    print(request.session['thisdata'])
    ImageID = request.GET.get('ImageTAG')

    # Get the Image that will be deleted and delete it , return to the project summary
    ImageWillDelete = ImageArtefact.objects.get(id=int(ImageID))
    print(ImageWillDelete.Image_Name)
    ImageWillDelete.delete()

    return HttpResponseRedirect(reverse('projectSummary'))


@login_required
def deleteVideo(request):
    print("Deleting Video")
    print(request.session['thisdata'])
    # Get the Current Video ID and Delete the Video
    VideoID = request.GET.get('VideoTAG')

    # Get the Video that will be deleted and delete it, then return to the project summary
    VideoWillDelete = VideoArtefact.objects.get(id=int(VideoID))
    print(VideoWillDelete.name)
    VideoWillDelete.delete()
    return HttpResponseRedirect(reverse('projectSummary'))


@login_required
def EditImage(request):
    print("Edit Image")
    # print(request.session['thisdata'])
    # Get the Current Image ID and Edit the Image
    ImageID = request.GET.get('ImageTAG')
    ImageWillEdit = ImageArtefact.objects.get(id=int(ImageID))
    if request.method == "POST":
        imageform = UploadImageForm(request.POST, request.FILES)
        TheImage = request.FILES.get('image')
        ImageName = request.POST.get('Image_Name')
        ImageDesc = request.POST.get('Image_Description')

        # Check if the image is changed or not
        # If the user does not upload a new image, it will stays the same
        if TheImage:
            print("Change the Image because it received a new image")
            ImageWillEdit.image = TheImage

        ImageWillEdit.Image_Name = ImageName
        ImageWillEdit.Image_Description = ImageDesc
        ImageWillEdit.save()
        print("Changed")

        return HttpResponseRedirect(reverse('projectSummary'))

    else:
        imageform = UploadImageForm()
        print("Load this as normal")
    return render(request, 'home_page/projectEditImage.html', {'ImageWillEdit': ImageWillEdit})


@login_required
def EditVideo(request):
    print("EditVideo")
    print(request.session['thisdata'])
    VideoID = request.GET.get('VideoTAG')
    VideoWillEdit = VideoArtefact.objects.get(id=int(VideoID))
    if request.method == "POST":

        VideoFile = request.FILES.get('videofile')
        VideoName = request.POST.get('name')
        VideoDesc = request.POST.get('Video_Description')
        VideoThumbnail = request.FILES.get('thumbnail')
        # Check if the image is changed or not

        if VideoFile:
            print("Change the Video because it received a new Video")
            VideoWillEdit.videofile = VideoFile
        else:
            print("The Video doesnt change")

        if VideoThumbnail:
            print("Change the Image because it received a new Image Thumbnail")
            VideoWillEdit.thumbnail = VideoThumbnail
        else:
            print("The Image doesnt change")

        VideoWillEdit.name = VideoName
        VideoWillEdit.Video_Description = VideoDesc
        VideoWillEdit.save()
        print("Changed")

        return HttpResponseRedirect(reverse('projectSummary'))
    else:

        print("Load this as normal")
    return render(request, 'home_page/projectEditVideo.html', {'VideoWillEdit': VideoWillEdit})


@login_required
def studentdashboard(request):
    thisuser = request.user


    # Get the current User ID , then get all the projects that belong to this User ID
    getCurrentUser = User.objects.prefetch_related().get(username=thisuser)
    getCurrentUserID = UserProfileInfo.objects.get(user_id=getCurrentUser.id)
    getUserProjects = Project.objects.filter(User_Owner_id=getCurrentUserID.id)
    # Cannot use .get() as it will only return 1 object , and if it tries to take more than 1
    # it will give some error

    # Get today Date to check if user can still edit or not DateField Object
    todayDate = date.today()

    # DateTime Object Is not needed for this type of website
    # todayDate = (timezone.now())
    # Get a dateField Object that is 7days , can be added or substracted to an existing DateField Object
    # nextweek = timedelta(days=7)
    # nextweekDate = todayDate + nextweek

    ProjectExists = False

    # Approval_Date
    if getUserProjects.exists():
        ProjectExists = True

    else:
        ProjectExists = False


    context = {'getUserProjects': getUserProjects,
               'ProjectExists': ProjectExists,
               'todayDate': todayDate}

    return render(request, 'home_page/studentdashboardcontent.html', context)


def ProjectView(request):
    print(request.session['thisdata'])
    # Get the Project that will be viewed, and all pictures and videos related to it
    CurrentProject = Project.objects.get(id=request.session['thisdata'])
    ProjectImages = ImageArtefact.objects.all().filter(Project_Owner=CurrentProject)
    ProjectVideos = VideoArtefact.objects.all().filter(Project_Owner=CurrentProject)
    # Return all Objects found to the page to be displayed
    return render(request, 'home_page/ProjectView.html',
                  {'CurrentProject': CurrentProject, 'ProjectImages': ProjectImages,
                   'ProjectVideos': ProjectVideos, })

def passToThisProject(request):
    imageID = request.GET.get("goToThisProject")
    request.session['thisdata'] = int(imageID)
    return HttpResponseRedirect(reverse('ProjectView'))

def error_404(request, exception):
    #return render(request, 'home_page/ivanoldlogin.html')
    # This will only be used if deployed on a server
    return HttpResponse("Page not Found")

# This special for now is useless
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
    return HttpResponseRedirect(reverse('homePage'))  # There is a problem here to return logout page
# After logout , redirect using here


@login_required
def register(request):
    if request.user.is_staff or request.user.is_superuser:
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

            # Connect the StudentID to the user table
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

                if user.is_superuser or user.is_staff:
                    print("Superuser or staff")
                    login(request, user)
                    # Send the user back to homepage.

                    return HttpResponseRedirect(reverse('register'))
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not staff or a superuser , please Login using that account.")
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


def searchbar(request):
    if request.method == "GET":
        search = request.GET.get('search')
        # This isn't particularly efficient... Too Bad!
        getCurrentUser = User.objects.prefetch_related().filter(Q(username__icontains=search))
        if getCurrentUser.exists():
            getCurrentUser = User.objects.prefetch_related().get(username=search)
            getCurrentUserID = UserProfileInfo.objects.get(user_id=getCurrentUser.id)
            context = Project.objects.all().filter(Q(User_Owner=getCurrentUserID)&Q(Project_Approval_Status = "Approved")).values('videoartefact__videofile','videoartefact__Video_Description','videoartefact__name','imageartefact__image','imageartefact__Image_Description','imageartefact__Image_Name','User_Owner','Project_Name')
        else:
            context = Project.objects.all().filter(Q(Project_Name__icontains=search) | Q(Project_Tag__icontains=search)).values('videoartefact__videofile','videoartefact__Video_Description','videoartefact__name','imageartefact__image','imageartefact__Image_Description','imageartefact__Image_Name','User_Owner','Project_Name')
        return render(request, 'home_page/searchbar.html', {"context":context})


# The test version Joseph
def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'home_page/uploadimagetest.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()

    return render(request, 'home_page/uploadimagetest.html', {'form': form})


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



def modulePage(request):
    moduleTag = request.GET.get('moduleTag')
    sortSetting = request.GET.get('sort')
    ProjectWithTag = Project.objects.all().filter(Q(Project_Tag__icontains=moduleTag)&Q(Project_Approval_Status = "Approved"))
    imageList = []
    for i in ProjectWithTag:
        tempFile = ImageArtefact.objects.all().filter(Project_Owner = i).values("image", "Project_Owner__Project_Name","Project_Owner__Project_Tag",'Project_Owner__Upload_Date','Project_Owner__id')[:2]
        if len(tempFile) == 2:
            imageList.append(tempFile)
        else:
            imageList.append(tempFile)

    if sortSetting == "latestUploaded":
        for i in range(0,len(imageList)-1):
            for j in range(0,len(imageList)-i-1):
                if imageList[j][0]['Project_Owner__Upload_Date'] < imageList[j + 1][0]['Project_Owner__Upload_Date']:
                    imageList[j], imageList[j+1] = imageList[j+1], imageList[j]
    # This is some magical python coding.
    elif sortSetting == "projectName":
        for i in range(0, len(imageList) - 1):
            for j in range(0, len(imageList) - i - 1):
                if imageList[j][0]['Project_Owner__Project_Name'] > imageList[j + 1][0]['Project_Owner__Project_Name']:
                    imageList[j], imageList[j + 1] = imageList[j + 1], imageList[j]

    module_paginator = Paginator(imageList, 15)
    page_num = request.GET.get('page')
    page = module_paginator.get_page(page_num)

    return render(request, 'home_page/modulePage.html', {"page": page, "tagName":moduleTag})


# def testID(request):
#     IDproject = request.GET.get('IDTAG')
#     print(IDproject)
#     context = Project.objects.all().filter(Q(id=IDproject)).values('videoartefact__videofile', 'videoartefact__Video_Description', 'videoartefact__name',  'imageartefact__image','imageartefact__Image_Description','imageartefact__Image_Name','User_Owner', 'Project_Name')
#     print(context)
#     #return all artefacts, and data of project
#     return render(request, 'home_page/modulePage.html', {})



#remember to return title not a number.

# def testProjectVideo(request):
#     bruh = request.session['thisdata']
#     print(bruh)
#     if request.method == 'POST':
#         form = VideoForm(request.POST, request.FILES)
#         if form.is_valid():
#
#             uploadedVideo = form.save(commit=False)
#             CurrentProject = Project.objects.get(id=request.session['thisdata'])
#             uploadedVideo.Project_Name = CurrentProject
#             uploadedVideo = form.save()
#             print("hai")
#             return HttpResponseRedirect(reverse('testProjectSummary'))
#         else:
#             print("Not valid")
#             print(form.errors.as_data())
#             # return render(request, 'home_page/register.html',
#
#             return render(request, 'home_page/testProjectVideo.html', {'Projectformhtml': Projectformhtml, 'form': form,
#                                                                        'imageform': imageform})
#
#     else:
#         Projectformhtml = ProjectForm()
#         form = VideoForm()
#         imageform = UploadImageForm()
#         return render(request, 'home_page/testProjectVideo.html', {'Projectformhtml': Projectformhtml, 'form': form,
#                                                                    'imageform': imageform})


def testProjectVideo(request):
    bruh = request.session['thisdata']
    print(bruh)
    if request.method == "POST":
        videos = request.FILES.getlist('videofile')
        vidname = request.POST.get('name')
        description = request.POST.get('Video_Description')
        CurrentProject = Project.objects.get(id=request.session['thisdata'])
        for vids in videos:
            videoArtefact = VideoArtefact.objects.create(Project_Owner=CurrentProject, name=vidname, videofile=vids,
                                                         Video_Description=description)

            videoArtefact.save()

            print("Saved")
        return HttpResponseRedirect(reverse('testProjectSummary'))

    else:
        Projectformhtml = ProjectForm()
        form = VideoForm()
        imageform = UploadImageForm()
        return render(request, 'home_page/testProjectVideo.html', {'form': form})


def testProjectImage(request):
    bruh = request.session['thisdata']
    print(bruh)
    if request.method == 'POST':
        imageform = UploadImageForm(request.POST, request.FILES)
        if imageform.is_valid():

            uploadedImage = imageform.save(commit=False)
            CurrentProject = Project.objects.get(id=request.session['thisdata'])
            uploadedImage.Project_Owner = CurrentProject
            uploadedImage = imageform.save()
            print("saved")
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
    print("Showing summary and project ID")
    print(request.session['thisdata'])
    CurrentProject = Project.objects.get(id=request.session['thisdata'])
    ProjectImages = ImageArtefact.objects.filter(Project_Owner=CurrentProject)
    ProjectVideos = VideoArtefact.objects.filter(Project_Owner=CurrentProject)
    print(CurrentProject)
    # print(CurrentProject.Project_Name)
    Projectformhtml = ProjectForm()
    form = VideoForm()
    imageform = UploadImageForm()
    print("Deleted BUTTON")
    ImageID = request.GET.get('ImageTAG')
    VideoID = request.GET.get('VideoTAG')

    print(ImageID)
    print(type(ImageID))

    print(VideoID)
    print(type(VideoID))
    if ImageID:
        print("waw image exist")
    if VideoID:
        print("waw video exist")

    if request.method == 'POST':
        VidID = request.POST.get('DeleteVid')
        ImgID = request.POST.get('DeleteImg')
        print("Video ID and type")
        print(VidID)
        print(type(VidID))
        # newint = int(VidID)
        # print(type(newint))
        print("Image ID and type")
        print(ImgID)
        print(type(ImgID))
        # newint2 = int(ImgID)
        print("Get the things responding to id")
        # ImageWillDelete = ImageArtefact.objects.get(id=newint2)
        # VideoWillDelete = VideoArtefact.objects.get(id=newint)
        # VideoWillDelete = ImageArtefact.objects.get(id=newint)
        # VideoWillDelete.delete()
        # print(ImageWillDelete.Image_Name)
    # print(VideoWillDelete.name)
    # ImageWillDelete.delete()
    return render(request, 'home_page/testProjectSummary.html', {'Projectformhtml': Projectformhtml, 'form': form,
                                                                 'imageform': imageform,
                                                                 'CurrentProject': CurrentProject
        , 'ProjectImages': ProjectImages, 'ProjectVideos': ProjectVideos})


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
            # print(EditedProject)
        return HttpResponseRedirect(reverse('testProjectSummary'))
    else:
        Projectformhtml = ProjectForm()
        print("No Changed")
    return render(request, 'home_page/testProjectDetailEdit.html',
                  {'Projectformhtml': Projectformhtml, 'CurrentProject': CurrentProject})

def homePage(request):
    sortSetting_homePage = request.GET.get('sort')
    if sortSetting_homePage == "latestUploaded":
        homePageArtefacts = ImageArtefact.objects.all().filter(Q(Project_Owner__Project_Approval_Status = "Approved")).values("image", "Image_Name", "Image_Description", "Project_Owner__Project_Name","Project_Owner__id").order_by("-Project_Owner__Upload_Date")
    elif sortSetting_homePage == "projectName":
        homePageArtefacts = ImageArtefact.objects.all().filter(Q(Project_Owner__Project_Approval_Status = "Approved")).values("image", "Image_Name", "Image_Description", "Project_Owner__Project_Name","Project_Owner__id").order_by("Image_Name")
    else:
        homePageArtefacts = ImageArtefact.objects.all().filter(Q(Project_Owner__Project_Approval_Status = "Approved")).values("image", "Image_Name", "Image_Description", "Project_Owner__Project_Name","Project_Owner__id")

    homepage_paginator = Paginator(homePageArtefacts, 9)
    page_num = request.GET.get('page')
    page = homepage_paginator.get_page(page_num)

    return render(request, 'home_page/homePage.html',{"page": page})




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
