from django.db import models
from datetime import datetime

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField(blank=True)
    img = models.ImageField(upload_to="image/")

    
