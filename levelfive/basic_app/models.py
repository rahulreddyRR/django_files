from django.db import models
#here we are importing user model from django which give you username,password,firstname,lastname,suername PREBuilt.
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #addtional if u want to any other requirments to USER model
    portpofolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self):
        return self.user.username
