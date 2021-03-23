from django.contrib import admin
from .models import User
# Register your models here.
from . import models
from .models import Project
from django.shortcuts import get_object_or_404


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
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        #print(obj)
        super().save_model(request, obj, form, change)

        # query for email here
        projectOwner = Project.objects.get(Project_Name=obj)
        userData = User.objects.get(username=projectOwner.User_Owner)
        if(projectOwner.Project_Approval_Status == "Rjct"):
            #due to localhost emails are not actually sent. For now we will substitute with an alert

            from django.contrib import messages
            messages.add_message(request, messages.INFO, 'Project Rejection email has been sent to ' + userData.email)
            # uncomment the part below if this website was to be deployed.
            # from django.core.mail import send_mail
            # send_mail(
            #     'Project Rejected',
            #     'Dear, student we are sorry to inform to you that your project has been rejected.',
            #     'from@example.com',
            #     [userData.email],
            #     fail_silently=False,
            # )


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
