from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# Admin Database is not needed cause we have superuser that can be created from here

# One User can have more than 1project
# ex I have Arduino Project to make the robot count binary up to 1000
# in that project I have multiple "Artefacts" or pictures/videos to show to the public
# Django supposed to create their own ID for us , so we do not need to put the IDs ,however we can override it
# Which one should we use ?

# class Student_User(models.Model):
# #No Longer used because Django have all of this pre built in
#     Account_Status_Choice = (
#         ('Act', 'Active'),
#         ('P', 'Pending'),
#         ('T', 'Terminated'),
#     )
#     # User_ID = models.PositiveIntegerField(unique = True)
#     User_Username = models.CharField(max_length=50, unique=True)
#     First_name = models.CharField(max_length=50)
#     Last_name = models.CharField(max_length=50)
#     StudentID = models.PositiveIntegerField(unique=True)
#     Date_Created = models.DateTimeField(default=timezone.now)
#     Account_Status = models.CharField(max_length=50, choices=Account_Status_Choice, default='Act')
#     Last_Online = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.User_Username


class UserProfileInfo(models.Model):
    # Add any extra information to connect with user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    StudentID = models.PositiveIntegerField(unique=True, default=0)
    #Date_Created , Account_Status and Last_Online is built-in Django Attributes in User

    # Testchar = models.CharField(max_length=50)
    # Add any additional attributes you want
    # portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    # profile_pic = models.ImageField(upload_to='basic_app/profile_pics', blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


class Project(models.Model):
    ApprovalChoice = [
        ('Apvd', 'Approved'),
        ('Pndg', 'Pending'),
        ('Rjct', 'Rejected'),
    ]
    # Project_ID = models.PositiveIntegerField(unique = True)
    #This is to connect , which Owner have dis project
    User_Owner = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, blank=True, null=True )

    Project_Name = models.CharField(max_length=50)
    Project_Description = models.TextField()
    Upload_Date = models.DateTimeField(default=timezone.now)
    Approval_Date = models.DateTimeField(blank=True, null=True)  # date cannot be null
    Last_Updated = models.DateTimeField(blank=True, null=True)
    Project_Approval_Status = models.CharField(max_length=32, choices=ApprovalChoice, default='Pndg')  # Approval
    Authors = models.CharField(max_length=100)

    def __str__(self):
        return self.Project_Name


# class Account_Project_Connector(models.Model):
#     User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
#     Project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.User_ID.username + ' ' + self.Project_ID.Project_Name


class Artefact_Info(models.Model):
    Project_Owner = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    ArtefactTypeChoice = [
        ('Vid', 'Video'),
        ('Pic', 'Picture'),
    ]  # these choices are kind of confusing
    # ArtefactID = models.PositiveIntegerField(unique = True)

    ArtefactType = models.CharField(max_length=50, choices=ArtefactTypeChoice)
    ArtefactName = models.CharField(max_length=50)
    ArtefactSize = models.CharField(max_length=50)  # might not be needed

    def __str__(self):
        return self.ArtefactName


# class Project_Artefact_Connector(models.Model):
#     Project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
#     Artefact_ID = models.ForeignKey(Artefact_Info, on_delete=models.CASCADE)


class Video_Artefact(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="") #path to video

    def __str__(self):
        return self.name + ": " + str(self.videofile)