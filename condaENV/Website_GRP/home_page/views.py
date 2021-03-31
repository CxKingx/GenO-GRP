from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home_page.models import VideoArtefact
from .forms import UserForm, UserProfileInfoForm, VideoForm, ProjectForm, UploadImageForm
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

# To be used by request
User = get_user_model()


# Create your views here.
# views for doing activities behind the scenes


# Return the first page for index
def landingPage(request):
    context = ImageArtefact.objects.all().order_by('Project_Owner__Upload_Date')[:13]
    # Get 13 most recent Pictures to be displayed to the landing page
    return render(request, 'home_page/landingPage.html', {"context": context})


# Takes User to Student Login Page
# Login request will be handled by user_login view
def loginPage(request):
    wrongpassword = True
    context = {'wrongpassword': wrongpassword}
    return render(request, 'home_page/StudentLogin.html', context)


# Takes User to Admin Login Page
def adminLogin(request):
    wrongpassword = True
    context = {'wrongpassword': wrongpassword}
    return render(request, 'home_page/adminLogin.html', context)


def contactUs(request):
    return render(request, 'home_page/contactUs.html', {})


# These 2 Layouts is used for extending the other content page
# So every page will contain elements from these 2 html without actually putting all html in each page
# It acts like css but it is html content
def layout(request):
    return render(request, 'home_page/layout.html', {})


def secondaryLayout(request):
    return render(request, 'home_page/secondaryLayout.html', {})


# This view is to handle the first step of the Upload , which is the details
@login_required
def ProjectUpload(request):
    if request.method == 'POST':
        # Get Data from User to be inserted to the object
        Projectformhtml = ProjectForm(request.POST, request.FILES)

        # Automatic check if the input is valid by Django
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

            # Reference the project to the user uploading it now and Save it
            uploadedProject.User_Owner = getCurrentUserID
            uploadedProject.save()
            # Set the ProjectID to the session data to be used by other views
            request.session['thisdata'] = uploadedProject.id

            return HttpResponseRedirect(reverse('projectSummary'))

        else:
            # errormessage = "Something Went Wrong when Uploading / You did not Upload any files"
            errorMessage = True
            print(Projectformhtml.errors.as_data())
            return render(request, 'home_page/projectUploadContent.html', {'errorMessage': errorMessage})

    else:
        # Pass on the empty form as a normal request
        Projectformhtml = ProjectForm()
    return render(request, 'home_page/projectUploadContent.html', {'Projectformhtml': Projectformhtml})


@login_required
def projectSummary(request):
    # Showing summary of the Project
    # request.session['thisdata']
    # Get the Project and its related artefacts that will be displayed in the summary
    CurrentProject = Project.objects.get(id=request.session['thisdata'])
    ProjectImages = ImageArtefact.objects.filter(Project_Owner=CurrentProject)
    ProjectVideos = VideoArtefact.objects.filter(Project_Owner=CurrentProject)

    return render(request, 'home_page/projectSummaryContent.html',
                  {'CurrentProject': CurrentProject, 'ProjectImages': ProjectImages, 'ProjectVideos': ProjectVideos})


# Edit the Details of the Project 'Name , Description , Authors, Date .....
@login_required
def editProjectDetail(request):
    # Edit Project detail

    # Get current project being edited
    CurrentProject = Project.objects.get(id=request.session['thisdata'])

    # Change the content of the Project Details into the new one
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
            # Project Detail Changed , now redirect back to summary
            # Return it back to Summary
            return HttpResponseRedirect(reverse('projectSummary'))
        else:
            # "Something Went Wrong when Uploading / You did not Upload any files"
            errorMessage = True
            return render(request, 'home_page/projectEditContent.html',
                          {'errorMessage': errorMessage})
    else:
        Projectformhtml = ProjectForm()
        # Load the Form with inputs already inserted
    return render(request, 'home_page/projectEditContent.html',
                  {'Projectformhtml': Projectformhtml, 'CurrentProject': CurrentProject})


# User wants to edit the project from student dashboard, so it will take the Project ID , and display it in the
# ProjectSummary Page
@login_required
def EditProject(request):
    # Editing Project
    # Get the corresponding ProjectID to be edited
    ProjectID = request.GET.get('ProjectTag')
    # Set the session to edit the Project with the ID
    request.session['thisdata'] = int(ProjectID)

    # Display it in the Project Summary page to be edited further
    return HttpResponseRedirect(reverse('projectSummary'))


@login_required
def ProjectUploadImage(request):
    # Uploading image
    # request.session['thisdata']
    # Get the Project that owns the Image File
    CurrentProject = Project.objects.get(id=request.session['thisdata'])
    # Check if the user pressed submit in the form
    if request.method == "POST":
        imageform = UploadImageForm(request.POST, request.FILES)
        # Check if the inputs are valid
        if imageform.is_valid():
            uploadedImage = imageform.save(commit=False)
            uploadedImage.Project_Owner = CurrentProject

            uploadedImage.save()
            # Image Saved
            # Return it back to Summary
            return HttpResponseRedirect(reverse('projectSummary'))
        else:
            # Failed to Upload
            # errormessage = "Something Went Wrong when Uploading / You did not Upload any files"
            errorMessage = True
            return render(request, 'home_page/uploadImageContent.html', {'errorMessage': errorMessage})

    else:
        # imageform = UploadImageForm()
        # Load this as a form for uploading image
        return render(request, 'home_page/uploadImageContent.html')


@login_required
def ProjectUploadVideo(request):
    # Get the project being edited from The Session Data
    # Uploading Video
    # request.session['thisdata']
    # Get the Project that owns the Video File
    CurrentProject = Project.objects.get(id=request.session['thisdata'])
    # Check if the user pressed submit in the form
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        # Check if the inputs are valid
        if form.is_valid():
            uploadedVideo = form.save(commit=False)
            uploadedVideo.Project_Owner = CurrentProject

            uploadedVideo.save()
            # Video is Saved
            # Return it back to Summary
            return HttpResponseRedirect(reverse('projectSummary'))
        else:
            # Not valid

            # "Something Went Wrong when Uploading / You did not Upload any files"
            errorMessage = True

            return render(request, 'home_page/uploadVideoContent.html', {'errorMessage': errorMessage})
    else:
        # Load an empty Video form page
        form = VideoForm()
    return render(request, 'home_page/uploadVideoContent.html', {'form': form})
    # return render(request, 'home_page/uploadVideoContent.html',{'form': form})


@login_required
def deleteImage(request):
    # Deleting Image
    # Get the Current Image ID and Delete the Image
    # request.session['thisdata']
    ImageID = request.GET.get('ImageTAG')

    # Get the Image that will be deleted and delete it , return to the project summary
    ImageWillDelete = ImageArtefact.objects.get(id=int(ImageID))

    ImageWillDelete.delete()

    return HttpResponseRedirect(reverse('projectSummary'))


@login_required
def deleteVideo(request):
    # Deleting Video
    # request.session['thisdata']
    # Get the Current Video ID and Delete the Video
    VideoID = request.GET.get('VideoTAG')

    # Get the Video that will be deleted and delete it, then return to the project summary
    VideoWillDelete = VideoArtefact.objects.get(id=int(VideoID))

    VideoWillDelete.delete()
    return HttpResponseRedirect(reverse('projectSummary'))


@login_required
def EditImage(request):
    # Edit Image
    # request.session['thisdata']
    # Get the Current Image ID and the Image object corresponds to it, then edit the Image
    ImageID = request.GET.get('ImageTAG')
    ImageWillEdit = ImageArtefact.objects.get(id=int(ImageID))
    if request.method == "POST":
        # imageform = UploadImageForm(request.POST, request.FILES)
        TheImage = request.FILES.get('image')
        ImageName = request.POST.get('Image_Name')
        ImageDesc = request.POST.get('Image_Description')

        # Check if the image is changed or not
        # If the user does not upload a new image, it will stays the same
        if TheImage:
            # Change the Image because it received a new image
            ImageWillEdit.image = TheImage
        # Change the remainder attributes to the input that is inserted by the user
        ImageWillEdit.Image_Name = ImageName
        ImageWillEdit.Image_Description = ImageDesc
        ImageWillEdit.save()
        # Image has Changed

        return HttpResponseRedirect(reverse('projectSummary'))

    else:
        # imageform = UploadImageForm()
        print("Load this as normal")
    return render(request, 'home_page/projectEditImage.html', {'ImageWillEdit': ImageWillEdit})


@login_required
def EditVideo(request):
    # EditVideo

    # Get the VideoID and the object corresponds to it , and edit it
    VideoID = request.GET.get('VideoTAG')
    VideoWillEdit = VideoArtefact.objects.get(id=int(VideoID))
    if request.method == "POST":

        VideoFile = request.FILES.get('videofile')
        VideoName = request.POST.get('name')
        VideoDesc = request.POST.get('Video_Description')
        VideoThumbnail = request.FILES.get('thumbnail')

        # Check if the Main Video and Thumbnail is changed or not

        if VideoFile:
            # Change the Video because it received a new Video
            VideoWillEdit.videofile = VideoFile
        # else:
            # The Video doesnt change

        if VideoThumbnail:
            # Change the Image because it received a new Image Thumbnail
            VideoWillEdit.thumbnail = VideoThumbnail
        # else:
            # The Image doesnt change

        # The other attributes will change as normal
        VideoWillEdit.name = VideoName
        VideoWillEdit.Video_Description = VideoDesc
        VideoWillEdit.save()
        # Changed the Database
        return HttpResponseRedirect(reverse('projectSummary'))
    else:
        print("Load this as normal")
    return render(request, 'home_page/projectEditVideo.html', {'VideoWillEdit': VideoWillEdit})


# Displays the projects that the user has uploaded and their details in a table
@login_required
def studentdashboard(request):
    thisuser = request.user
    # Get the current User ID , then get all the projects that belong to this User ID
    getCurrentUser = User.objects.prefetch_related().get(username=thisuser)
    getCurrentUserID = UserProfileInfo.objects.get(user_id=getCurrentUser.id)
    getUserProjects = Project.objects.filter(User_Owner_id=getCurrentUserID.id)
    # Cannot use .get() as it will only return 1 object , and if it tries to take more than 1
    # it will give some error, so we use filter to get multiple objects

    # Get today Date to check if user can still edit or not DateField Object
    todayDate = date.today()
    # ProjectExists = False

    if getUserProjects.exists():
        ProjectExists = True

    else:
        ProjectExists = False

    context = {'getUserProjects': getUserProjects,
               'ProjectExists': ProjectExists,
               'todayDate': todayDate}

    return render(request, 'home_page/studentdashboardcontent.html', context)


# Show a specific project detail with all the pictures and videos related to it
def ProjectView(request):

    # Get the Project that will be viewed, and all pictures and videos related to it
    CurrentProject = Project.objects.get(id=request.session['thisdata'])
    ProjectImages = ImageArtefact.objects.all().filter(Project_Owner=CurrentProject)
    ProjectVideos = VideoArtefact.objects.all().filter(Project_Owner=CurrentProject)
    # Return all Objects found to the page to be displayed
    return render(request, 'home_page/ProjectView.html',
                  {'CurrentProject': CurrentProject, 'ProjectImages': ProjectImages,
                   'ProjectVideos': ProjectVideos, })


# Get the Project ID that wants to be viewed by clicking on the Image Learn more , then show it in the Project View
def passToThisProject(request):
    imageID = request.GET.get("goToThisProject")
    request.session['thisdata'] = int(imageID)
    return HttpResponseRedirect(reverse('ProjectView'))


# Show this is A page is not found
def error_404(request, exception):
    # This will only be used if deployed on a server
    return HttpResponse("Page not Found")


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('landingPage'))  # There is a problem here to return logout page


@login_required
def register(request):
    # Check if user is staff or admin , if it is not , return them to the admin login page
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
            profile.save()

            registered = True
            # Registered

            return render(request, 'home_page/registerSuccess.html', {'registered': registered})

        else:
            # One of the forms was invalid if this else gets called.

            print(user_form.errors.as_data(), profile_form.errors.as_data())
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
            # User inserted an invalid account / input the wrong credentials
            wrongpassword = False
            context = {'wrongpassword': wrongpassword}
            return render(request, 'home_page/StudentLogin.html', context)

    else:
        # Nothing has been provided for username or password.
        return render(request, 'home_page/StudentLogin.html', {})


def admin_login(request):
    # admin login
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
                # Check if user is staff or superuser
                if user.is_superuser or user.is_staff:
                    # Superuser or staff has logged in
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
            # User inserted an invalid account / input the wrong credentials
            wrongpassword = False
            context = {'wrongpassword': wrongpassword}
            return render(request, 'home_page/accountRegistration.html', context)

    else:
        # Nothing has been provided for username or password.
        return render(request, 'home_page/adminLogin.html', {})


# Function to check input from search bar.
def searchbar(request):
    if request.method == "GET":
        search = request.GET.get('search')
        # This isn't particularly efficient... Too Bad!
        getCurrentUser = User.objects.prefetch_related().filter(Q(username__icontains=search))
        # The if clause below checks if the string inputted is an existing user.
        # If it is then then it wil query from user name, else it will use the Project Name or tag.
        if getCurrentUser.exists():
            getCurrentUser = User.objects.prefetch_related().get(username=search)
            getCurrentUserID = UserProfileInfo.objects.get(user_id=getCurrentUser.id)
            context = Project.objects.all().filter(
                Q(User_Owner=getCurrentUserID) & Q(Project_Approval_Status="Approved")).values(
                'videoartefact__videofile', 'videoartefact__Video_Description', 'videoartefact__name',
                'imageartefact__image', 'imageartefact__Image_Description', 'imageartefact__Image_Name', 'User_Owner',
                'Project_Name')
        else:
            context = Project.objects.all().filter(
                Q(Project_Name__icontains=search) | Q(Project_Tag__icontains=search)).values('videoartefact__videofile',
                                                                                             'videoartefact__Video_Description',
                                                                                             'videoartefact__name',
                                                                                             'imageartefact__image',
                                                                                             'imageartefact__Image_Description',
                                                                                             'imageartefact__Image_Name',
                                                                                             'User_Owner',
                                                                                             'Project_Name')
        return render(request, 'home_page/searchbar.html', {"context": context})


# Returns a page consisting of all artefacts in that module
def modulePage(request):
    moduleTag = request.GET.get('moduleTag')
    sortSetting = request.GET.get('sort')
    ProjectWithTag = Project.objects.all().filter(
        Q(Project_Tag__icontains=moduleTag) & Q(Project_Approval_Status="Approved"))
    imageList = []
    for i in ProjectWithTag:
        tempFile = ImageArtefact.objects.all().filter(Project_Owner=i).values("image", "Project_Owner__Project_Name",
                                                                              "Project_Owner__Project_Tag",
                                                                              'Project_Owner__Upload_Date',
                                                                              'Project_Owner__id')[:2]
        # Query the objects and input it into a list.
        if len(tempFile) == 2:
            imageList.append(tempFile)
        else:
            imageList.append(tempFile)
    # Sort it by the variable sortSetting, either by project upload date or alphabetical
    if sortSetting == "latestUploaded":
        for i in range(0, len(imageList) - 1):
            for j in range(0, len(imageList) - i - 1):
                if imageList[j][0]['Project_Owner__Upload_Date'] < imageList[j + 1][0]['Project_Owner__Upload_Date']:
                    imageList[j], imageList[j + 1] = imageList[j + 1], imageList[j]
    # This is some magical python coding.
    elif sortSetting == "projectName":
        for i in range(0, len(imageList) - 1):
            for j in range(0, len(imageList) - i - 1):
                if imageList[j][0]['Project_Owner__Project_Name'] > imageList[j + 1][0]['Project_Owner__Project_Name']:
                    imageList[j], imageList[j + 1] = imageList[j + 1], imageList[j]
    # Code to return the data in pages, currently set to return 15 objects per page.
    module_paginator = Paginator(imageList, 15)
    page_num = request.GET.get('page')
    page = module_paginator.get_page(page_num)

    return render(request, 'home_page/modulePage.html', {"page": page, "tagName": moduleTag})


# Returns home page, which shows all the projects.
def homePage(request):
    sortSetting_homePage = request.GET.get('sort')
    # Returns a query according to the picked sort button.
    if sortSetting_homePage == "latestUploaded":
        homePageArtefacts = ImageArtefact.objects.all().filter(
            Q(Project_Owner__Project_Approval_Status="Approved")).values("image", "Image_Name", "Image_Description",
                                                                         "Project_Owner__Project_Name",
                                                                         "Project_Owner__id").order_by(
            "-Project_Owner__Upload_Date")
    elif sortSetting_homePage == "projectName":
        homePageArtefacts = ImageArtefact.objects.all().filter(
            Q(Project_Owner__Project_Approval_Status="Approved")).values("image", "Image_Name", "Image_Description",
                                                                         "Project_Owner__Project_Name",
                                                                         "Project_Owner__id").order_by("Image_Name")
    else:
        homePageArtefacts = ImageArtefact.objects.all().filter(
            Q(Project_Owner__Project_Approval_Status="Approved")).values("image", "Image_Name", "Image_Description",
                                                                         "Project_Owner__Project_Name",
                                                                         "Project_Owner__id")
    # Paging function.
    homepage_paginator = Paginator(homePageArtefacts, 9)
    page_num = request.GET.get('page')
    page = homepage_paginator.get_page(page_num)

    return render(request, 'home_page/homePage.html', {"page": page})
