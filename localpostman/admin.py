from django.contrib import admin

from localpostman.models import jarvis_requested_access, jarvis_user, jarvis_videoaccess,jarvis_gptaccess,jarvis_musicaccess,Music
# Register your models here.

admin.site.register(jarvis_user)
admin.site.register(jarvis_requested_access)
admin.site.register(jarvis_videoaccess)
admin.site.register(jarvis_gptaccess)
admin.site.register(jarvis_musicaccess)
admin.site.register(Music)
