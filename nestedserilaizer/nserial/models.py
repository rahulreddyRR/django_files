from django.db import models

# Create your models here.
class Auther(models.Model):
    firstname = models.CharField(blank=False, max_length=100)
    lastname = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.firstname,self.lastname

class Book(models.Model):
    title = models.CharField(blank=False, max_length=100)
    rating = models.CharField(blank=False, max_length=100)
    auther = models.ForeignKey(Auther,related_name='books',on_delete=models.CASCADE)
