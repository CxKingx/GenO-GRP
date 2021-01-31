from django.db import models
from django.utils import timezone


# Create your models here.
# Admin Database is not needed cause we have superuser that can be created from here

# One User can have more than 1project
# ex I have Arduino Project to make the robot count binary up to 1000
# in that project I have multiple "Artefacts" or pictures/videos to show to the public
# Django supposed to create their own ID for us , so we do not need to put the IDs ,however we can override it if we want
# Which one should we use ?

class User(models.Model):
    Account_Status_Choice = (
        ('Act', 'Active'),
        ('P', 'Pending'),
        ('T', 'Terminated'),
    )
    # User_ID = models.PositiveIntegerField(unique = True)
    User_Username = models.CharField(max_length=50, unique=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    StudentID = models.PositiveIntegerField(unique=True)
    Date_Created = models.DateTimeField(default=timezone.now)
    Account_Status = models.CharField(max_length=50, choices=Account_Status_Choice, default='Act')
    Last_Online = models.DateTimeField()

    def __str__(self):
        return self.User_Username


class login_credential(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    User_Username = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=50)


#
class Project(models.Model):
    ApprovalChoice = [
        ('Apvd', 'Approved'),
        ('Pndg', 'Pending'),
        ('Rjct', 'Rejected'),
    ]
    # Project_ID = models.PositiveIntegerField(unique = True)
    Project_Name = models.CharField(max_length=50)
    Project_Description = models.TextField()
    Upload_Date = models.DateTimeField(default=timezone.now)
    Approval_Date = models.DateTimeField(blank=True, null=True) #date cannot be null
    Last_Updated = models.DateTimeField(blank=True, null=True)
    Project_Approval_Status = models.CharField(max_length=32, choices=ApprovalChoice, default='Pndg')  # Approval
    Authors = models.CharField(max_length=100)

    def __str__(self):
        return self.Project_Name


class Account_Project_Connector(models.Model):
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)


class Artefact_Info(models.Model):
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


class Project_Artefact_Connector(models.Model):
    Project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    Artefact_ID = models.ForeignKey(Artefact_Info, on_delete=models.CASCADE)
