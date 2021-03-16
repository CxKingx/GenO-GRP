from django.contrib import admin
# from .models import User, login_credential, Project, Account_Project_Connector, Project_Artefact_Connector, Artefact_Info
# Register your models here.
from . import models


# admin.site.register()

# class UserAdmin(admin.ModelAdmin):
#     search_fields = ['User_Username']
#
#     list_display = ['User_Username','StudentID'] #add display as u wish
#
#     list_filter =['User_Username','StudentID']
#
#     list_editable =['StudentID']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['User_Owner', 'Project_Name','Project_Tag', 'Upload_Date', 'Project_Approval_Status']
    search_fields = ['Project_Name', 'Project_Approval_Status','Project_Tag']
    list_editable = ['Project_Approval_Status']


class ArtefactAdmin(admin.ModelAdmin):
    list_display = ['Project_Owner','Image_Name' , 'image']
    search_fields = ['Image_Name']


class StudentIDAdmin(admin.ModelAdmin):
    list_display = ['user', 'StudentID']
    search_fields = ['StudentID']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['Project_Owner','name' , 'videofile']
    search_fields = ['name']


# admin.site.register(models.Student_User, UserAdmin)
admin.site.register(models.UserProfileInfo, StudentIDAdmin)
# admin.site.register(models.login_credential)
admin.site.register(models.Project, ProjectAdmin)
# admin.site.register(models.Account_Project_Connector)
# admin.site.register(models.Project_Artefact_Connector)
admin.site.register(models.Image_Artefact, ArtefactAdmin)
admin.site.register(models.Video_Artefact,VideoAdmin)
