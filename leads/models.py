from xxlimited import Str
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)

class Lead(models.Model):
    ismi = models.CharField(max_length=20)
    familyasi = models.CharField(max_length=20)
    yoshi = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", blank = True, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.familyasi)



class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user)