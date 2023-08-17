"""
URL configuration for localpostman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from localpostman.views import checkjarvis_user, create_user, jarvis,checkjarvis_gptaccess,checkjarvis_musicaccess,checkjarvis_videoaccess

urlpatterns = [
    path("admin/", admin.site.urls),
    path('jarvis/', jarvis, name='jarvis'),
    path('jarvisCheckUser/',checkjarvis_user,name='checkjarvis_user'),
    path('jarvisCreateUser/',create_user,name="create_user"),
    path('checkjarvis_gptaccess/', checkjarvis_gptaccess, name="checkjarvis_gptaccess"),
    path('checkjarvis_musicaccess/', checkjarvis_musicaccess, name="checkjarvis_musicaccess"),
    path('checkjarvis_videoaccess/', checkjarvis_videoaccess, name="checkjarvis_videoaccess"),
]
