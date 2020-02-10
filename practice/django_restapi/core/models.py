from django.db import models

# Create your models here.

class students(models.Model):
    name = models.CharField(blank=True, max_length=100)
    marks = models.IntegerField(blank=True, null=True)
