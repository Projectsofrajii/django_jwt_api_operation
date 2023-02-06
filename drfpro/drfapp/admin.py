from django.contrib import admin

# Register your models here.

from .models import RsmUserMaster,RsmRoleMaster

admin.site.register(RsmUserMaster)
admin.site.register(RsmRoleMaster)