from django.contrib import admin

from localpostman.models import jarvis_requested_access, jarvis_user
# Register your models here.

admin.site.register(jarvis_user)
admin.site.register(jarvis_requested_access)
