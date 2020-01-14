from django.db import models

# Create your models here.
class User(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)

    def __str__(self):
        return self.First_name
