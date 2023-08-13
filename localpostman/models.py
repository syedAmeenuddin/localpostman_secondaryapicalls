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
