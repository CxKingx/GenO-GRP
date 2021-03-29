from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from validators import validate_image_size


# Create your models here.
# These are the building blocks for the database

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
    ModuleNames = [
        ('Data Scholarship', 'Data Scholarship'),
        ('Digital Media Production', 'Digital Media Production'),
        ('Technologies for Learning', 'Technologies for Learning'),
    ]

    # This is to connect , which Owner have this project
    User_Owner = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, blank=True, null=True)

    Project_Name = models.CharField(max_length=100)
    Project_Description = models.TextField()
    Project_Tag = models.CharField(max_length=32, choices=Tags_for_Project, default='', blank=True, null=True)
    Module_Name = models.CharField(max_length=32, choices=ModuleNames,default='Data Scholarship', blank=True, null=True)
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

    Image_Name = models.CharField(max_length=100)
    Image_Description = models.TextField()
    image = models.ImageField(upload_to='artefacts/', null=True, verbose_name="")

    def __str__(self):
        return self.Image_Name


class VideoArtefact(models.Model):
    # Links to the Project for this artefact
    Project_Owner = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=100)
    Video_Description = models.TextField(null=True)
    videofile = models.FileField(upload_to='artefacts/', null=True, verbose_name="")  # path to video
    thumbnail = models.ImageField(upload_to='artefacts/', null=True, verbose_name="")
    def __str__(self):
        return self.name + ": " + str(self.videofile)


class Image(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', null=True, verbose_name="", validators=[validate_image_size])

    def __str__(self):
        return self.title

# pip install pillow to use this!
# Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
# image = models.ImageField(upload_to='basic_app/profile_pics', blank=True) z
