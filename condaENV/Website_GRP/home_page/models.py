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
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    StudentID = models.PositiveIntegerField(unique=True, default=0)


    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


class Project(models.Model):
    ApprovalChoice = [
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    ]
    Tags_for_Project = [
        ('', '-----'),
        ('Data Scholarship', 'Data Scholarship'),
        ('Digital Media Production', 'Digital Media Production'),
        ('Technologies for Learning', 'Technologies for Learning'),
    ]

    # This is to connect , which Owner have this project
    User_Owner = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, blank=True, null=True)

    Project_Name = models.CharField(max_length=50)
    Project_Description = models.TextField()
    Project_Tag = models.CharField(max_length=32, choices=Tags_for_Project, default='', blank=True, null=True)

    Date_of_Completion = models.DateField(default=timezone.now)
    Author_Comment = models.TextField(blank=True, null=True)

    Upload_Date = models.DateField(default=timezone.now)
    Approval_Date = models.DateField(blank=True, null=True)
    # Make Expire Date 2weeks after upload , code in views.py, after approve no change
    Account_ExpiryDate = models.DateField(blank=True, null=True)
    Last_Updated = models.DateField(blank=True, null=True)

    Project_Approval_Status = models.CharField(max_length=32, choices=ApprovalChoice, default='Pending')  # Approval
    Authors = models.CharField(max_length=100, blank=True, null=True)

    Admin_Comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Project_Name


class ImageArtefact(models.Model):
    # Links to the Project for this artefact
    Project_Owner = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    Image_Name = models.CharField(max_length=50)
    Image_Description = models.TextField()
    image = models.ImageField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.Image_Name



class VideoArtefact(models.Model):
    # Links to the Project for this artefact
    Project_Owner = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=50)
    Video_Description = models.TextField(null=True)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")  # path to video

    def __str__(self):
        return self.name + ": " + str(self.videofile)


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.title

# pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    # image = models.ImageField(upload_to='basic_app/profile_pics', blank=True)
