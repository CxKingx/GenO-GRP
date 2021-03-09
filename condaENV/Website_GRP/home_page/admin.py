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
    search_fields = ['Project_Name']


class ArtefactAdmin(admin.ModelAdmin):
    search_fields = ['ArtefactName']
# models.


# admin.site.register(models.Student_User, UserAdmin)
admin.site.register(models.UserProfileInfo)
# admin.site.register(models.login_credential)
admin.site.register(models.Project, ProjectAdmin)
#admin.site.register(models.Account_Project_Connector)
#admin.site.register(models.Project_Artefact_Connector)
admin.site.register(models.Artefact_Info, ArtefactAdmin)
