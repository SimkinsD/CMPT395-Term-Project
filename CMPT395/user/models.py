from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.conf import settings

class MyUserManager(UserManager):
    pass

class MyUser(AbstractUser):
    objects = MyUserManager()
    current_person = None

class Teacher(MyUser):
    objects = MyUserManager()
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

class Person(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='person')
    name = models.CharField(max_length=32)
    hours = models.FloatField(default=5.0)
    
    def __str__(self):
        return self.name

class Children(models.Model):
    name = models.CharField(max_length=30)
    class_room = models.CharField(max_length=30)


class ChooseFacilitator(models.Model):
    name = models.CharField(max_length=30)
    hours = models.FloatField(default=0)

    def __str__(self):
        return 'Current Person'