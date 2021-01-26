from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    Account_Status_Choice = (
        ('A' , 'Active'),
        ('P' , 'Pending'),
        ('T' , 'Terminated'),
    )
    UserID = models.PositiveIntegerField() #Unique
    User_Username = models.CharField(max_length=50)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    StudentID = models.PositiveIntegerField()
    Date_Created = models.DateTimeField(default=timezone.now)
    Account_Status =
    Last_Online  models.DateTimeField(default=timezone.now)

class login_credential (models.Model):
    User_Username = models.CharField(max_length=50)
    Password = models.CharField (max_length=50)

class Project (models.Model):
    ApprovalChoice = (
        ('Apvd', 'Approved'),
        ('Pndg', 'Pending'),
        ('Rjct', 'Rejected'),
    )
    ProjectID = models.PositiveIntegerField() #Unique
    Project_Name = models.CharField(max_length=50)
    Project_Description = models.CharField(max_length=255)
    Upload_Date = models.DateTimeField(default=timezone.now)
    Approval_Date = models.DateTimeField(default=timezone.now)
    Last_Updated = models.DateTimeField(default=timezone.now)
    Project_Approval_Status = #Approval Choice
    Authors = models.CharField(max_length=100)

#class Account_Project Connector
 # User ID Project ID

#Class Project Artefact Connector
 #Project ID Artefact ID

class ArtefactInfo(models.Model):
    ArtefactTypeChoice = (
        ('Vid','Video'),
        ('Pic','Picture'),
    )
    ArtefactID =
    ArtefactType =
    ArtefactName = models.CharField(max_length=50)
