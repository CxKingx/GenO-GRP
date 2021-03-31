from django.contrib import admin
from . import models
from .models import Project, User

# Register your models here.
# The Admin file is to show the Admin what will be displayed from the Database
# Then we can change how the admin looks in the table by giving out Django Built in features
# Example list_display , search_fields , list_editable and list_filter


class StudentIDAdmin(admin.ModelAdmin):
    list_display = ['user', 'StudentID']
    search_fields = ['StudentID']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['User_Owner', 'Project_Name', 'Project_Tag', 'Upload_Date', 'Project_Approval_Status']
    search_fields = ['Project_Name', 'Project_Approval_Status', 'Project_Tag', 'User_Owner__user__username']
    list_editable = ['Project_Approval_Status']
    list_filter = ['Project_Approval_Status','Project_Tag','User_Owner__user__username']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        #print(obj)
        super().save_model(request, obj, form, change)

        # query for email here
        projectOwner = Project.objects.get(Project_Name=obj)
        userData = User.objects.get(username=projectOwner.User_Owner)
        if(projectOwner.Project_Approval_Status == "Rejected"):
            #due to localhost emails are not actually sent. For now we will substitute with an alert

            from django.contrib import messages
            messages.add_message(request, messages.INFO, 'Project rejection email has been sent to ' + userData.email)
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
    list_display = ['Project_Owner', 'Image_Name', 'image']
    search_fields = ['Image_Name', 'Project_Owner__Project_Name','Project_Owner__User_Owner__user__username']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['Project_Owner', 'name', 'videofile']
    search_fields = ['name','Project_Owner__Project_Name','Project_Owner__User_Owner__user__username']



admin.site.register(models.UserProfileInfo, StudentIDAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ImageArtefact, ArtefactAdmin)
admin.site.register(models.VideoArtefact, VideoAdmin)

#https://docs.djangoproject.com/en/3.1/ref/contrib/admin/actions/

# like make all project into approve / rejected / pending
# or u want to disable with disable_action