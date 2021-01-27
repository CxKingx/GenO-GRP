from django.db import models
from django.utils import timezone

# Create your models here.
# Admin Database is not needed cause we have superuser that can be created from here

# class User(models.Model):
#     Account_Status_Choice = (
#         ('Act' , 'Active'),
#         ('P' , 'Pending'),
#         ('T' , 'Terminated'),
#     )
#     User_ID = models.PositiveIntegerField(unique = True)
#     User_Username = models.CharField(max_length=50)
#     First_name = models.CharField(max_length=50)
#     Last_name = models.CharField(max_length=50)
#     StudentID = models.PositiveIntegerField(unique = True)
#     Date_Created = models.DateTimeField(default=timezone.now)
#     Account_Status =models.CharField(max_length=50 , choices = Account_Status_Choice , default = 'Act')
#     Last_Online  models.DateTimeField(default=timezone.now)
#
# class login_credential (models.Model):
#     User_Username = models.CharField(max_length=50)
#     Password = models.CharField (max_length=50)
#
# class Project (models.Model):
#     ApprovalChoice = [
#         ('Apvd', 'Approved'),
#         ('Pndg', 'Pending'),
#         ('Rjct', 'Rejected'),
#     ]
#     Project_ID = models.PositiveIntegerField(unique = True) #Unique
#     Project_Name = models.CharField(max_length=50)
#     Project_Description = models.CharField(max_length=255)
#     Upload_Date = models.DateTimeField(default=timezone.now)
#     Approval_Date = models.DateTimeField(default=timezone.now)
#     Last_Updated = models.DateTimeField(default=timezone.now)
#     Project_Approval_Status = models.CharField(max_length=32 , choices = ApprovalChoice , default = 'Pndg') #Approval
#     Authors = models.CharField(max_length=100)
#
# class Account_Project_Connector
#  # User_ID = models.PositiveIntegerField()
#  # Project_ID = models.PositiveIntegerField(unique = True)
#
# #class Project Artefact Connector
#  Project ID = models.PositiveIntegerField(unique = True)
#  Artefact ID = models.PositiveIntegerField(unique = True)
#
# class ArtefactInfo(models.Model):
#     ArtefactTypeChoice = [
#         ('Vid','Video'),
#         ('Pic','Picture'),
#     ]
#     ArtefactID = models.PositiveIntegerField(unique = True)
#     ArtefactType = models.CharField(max_length=50 , choices = ArtefactTypeChoice )
#     ArtefactName = models.CharField(max_length=50)
