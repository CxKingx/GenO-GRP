from django.contrib import admin
from .models import User, login_credential, Project, Account_Project_Connector, Project_Artefact_Connector, Artefact_Info
# Register your models here.

#admin.site.register()
admin.site.register(User)
admin.site.register(login_credential)
admin.site.register(Project)
admin.site.register(Account_Project_Connector)
admin.site.register(Project_Artefact_Connector)
admin.site.register(Artefact_Info)
