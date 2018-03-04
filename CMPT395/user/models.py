from django.contrib.auth.models import AbstractUser, UserManager, User
from django.db import models
from django.conf import settings


# Need Django's User creator here. It will link with the family class
class MyUserManager(UserManager):
    pass

class MyUser(AbstractUser):
    objects = MyUserManager()

# Need to add MyUser to this
class Family(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fID = models.AutoField(primary_key=True)
    family_name = models.CharField(max_length=50)
    #phone = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.family_name


# Code from https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Child(models.Model):
    cID = models.AutoField(primary_key=True)
    famID = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    family_name = models.CharField(max_length=25)
    classroom = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s' % (self.first_name, self.family_name)


class Volunteer(models.Model):
    vID = models.AutoField(primary_key=True)
    fID = models.ForeignKey(Family, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    #phone = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)



class Signup(models.Model):
    sID = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    vID = models.ForeignKey(Volunteer, on_delete= models.CASCADE)

    def __str__(self):
        return self.sID


#class PhoneNumbers(models.Model):
#    pID = models.AutoField(primary_key=True)
#    type = models.CharField(max_length=25)
#    # Solution for phone numbers from https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
#    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list


#    def __str__(self):
#        return self.phone_number