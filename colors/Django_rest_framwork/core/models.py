from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(blank=False, max_length=100)
    score = models.IntegerField(blank=False, null=False)
    
