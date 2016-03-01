from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.
class school(models.Model):


    name = models.CharField(max_length =200) 
    city = models.CharField(max_length = 200)
    since = models.DateField(default=timezone.now())
    schoolid= models.IntegerField(default=None)
    primary= models.NullBooleanField()
    secondary=models.NullBooleanField()
    senior= models.NullBooleanField()       
    desc=models.TextField(default=None)


    def __str__(self):
        return self.name