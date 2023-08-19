from django.db import models

class jarvis_user(models.Model):
    username = models.CharField(max_length=100, unique=True)
    passcode = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.username

class jarvis_requested_access(models.Model):
    username = models.CharField(max_length=20, unique=True)
    passcode = models.CharField(max_length=20) 
    message = models.CharField(max_length=100)
    def __str__(self):
        return self.username
    
class jarvis_gptaccess(models.Model):
    user = models.ForeignKey(jarvis_user,on_delete=models.CASCADE,blank=False,null=False)
    access = models.BooleanField(default=False, blank=False)
    def __str__(self):
        return str(self.user)
class jarvis_musicaccess(models.Model):
    user = models.ForeignKey(jarvis_user,on_delete=models.CASCADE,blank=False,null=False)
    access = models.BooleanField(default=False, blank=False)
    def __str__(self):
        return str(self.user)
class jarvis_videoaccess(models.Model):
    user = models.ForeignKey(jarvis_user,on_delete=models.CASCADE,blank=False,null=False)
    access = models.BooleanField(default=False, blank=False)
    def __str__(self):
        return str(self.user)
class Music(models.Model):
    user = models.ForeignKey(jarvis_user,on_delete=models.CASCADE,blank=False,null=False)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='listening/')

    def __str__(self):
        return self.title
  

