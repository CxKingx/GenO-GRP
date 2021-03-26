from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo, VideoArtefact, Image, Project, ImageArtefact


# this is for asking forms from models we have created

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')  # can add first name last name


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('StudentID',)


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoArtefact
        fields = ["name",'Video_Description', "videofile"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('Project_Name', 'Project_Description', 'Project_Tag', 'Date_of_Completion', 'Author_Comment',
                  'Authors' , 'Module_Name')
        # Upload_Date Approval_Date Account_ExpiryDate Last_Updated Project_Approval_Status


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = ImageArtefact
        fields = ('Image_Name', 'Image_Description', 'image')


# Joseph's Image Artefact , should not be used as the models is not complete
class ImageForm(forms.ModelForm):
    """Form for image folder"""

    class Meta:
        model = Image
        fields = ('title', 'image')
