from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo, VideoArtefact, Project, ImageArtefact


# Forms is used to ease validation from the used
# by calling  Form.is_valid() we can easily check the content of the input and automatically give out error
# if an error occur / invalid input was inserted

# Call by giving out the Meta() models , and insert the fields that needs to get input from user


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
        fields = ["name",'Video_Description', "videofile", "thumbnail"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('Project_Name', 'Project_Description', 'Project_Tag', 'Date_of_Completion', 'Author_Comment',
                  'Authors' , 'Module_Name')


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = ImageArtefact
        fields = ('Image_Name', 'Image_Description', 'image')
