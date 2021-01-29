from django.db import models
from django.utils import timezone

# Create your models here.
# Admin Database is not needed cause we have superuser that can be created from here

#One User can have more than 1project
# ex I have Arduino Project to make the robot count binary up to 1000
# in that project I have multiple "Artefacts" or pictures/videos to show to the public


# class User(models.Model):
#     Account_Status_Choice = (
#         ('Act' , 'Active'),
#         ('P' , 'Pending'),
#         ('T' , 'Terminated'),
#     )
#    # User_ID = models.PositiveIntegerField(unique = True)
#     User_Username = models.CharField(max_length=50)
#     First_name = models.CharField(max_length=50)
#     Last_name = models.CharField(max_length=50)
#     StudentID = models.PositiveIntegerField(unique = True)
#     Date_Created = models.DateTimeField(default=timezone.now)
#     Account_Status =models.CharField(max_length=50 , choices = Account_Status_Choice , default = 'Act')
#     Last_Online  models.DateTimeField()
#
# class login_credential (models.Model):
#       UserID = models.ForeignKey(User)
#     User_Username = models.CharField(max_length=50)
#     Password = models.CharField (max_length=50)
#
# class Project (models.Model):
#     ApprovalChoice = [
#         ('Apvd', 'Approved'),
#         ('Pndg', 'Pending'),
#         ('Rjct', 'Rejected'),
#     ]
#      # Project_ID = models.PositiveIntegerField(unique = True)
#     Project_Name = models.CharField(max_length=50)
#     Project_Description = models.TextField()
#     Upload_Date = models.DateTimeField(default=timezone.now)
#     Approval_Date = models.DateTimeField()
#     Last_Updated = models.DateTimeField()
#     Project_Approval_Status = models.CharField(max_length=32 , choices = ApprovalChoice , default = 'Pndg') #Approval
#     Authors = models.CharField(max_length=100)
#
# class Account_Project_Connector
#  # User_ID = models.ForeignKey(User)
#  # Project_ID = models.ForeignKey(Project)
#
# class Project Artefact Connector
#  Project_ID = models.ForeignKey(Project)
#  Artefact_ID = models.ForeignKey(ArtefactInfo)
#
# class ArtefactInfo(models.Model):
#     ArtefactTypeChoice = [
#         ('Vid','Video'),
#         ('Pic','Picture'),
#     ] #these choices are kind of confusing
#     ArtefactID = models.PositiveIntegerField(unique = True)
#     ArtefactType = models.CharField(max_length=50 , choices = ArtefactTypeChoice )
#     ArtefactName = models.CharField(max_length=50)
#     ArtefactSize = models.CharField(max_length=50) #might not be needed
