from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
   first_name = models.CharField(max_length=50)#Varchar
   last_name = models.CharField(max_length=50,blank=True)
   phone = models.CharField(max_length=9)
   email = models.EmailField(max_length=254, blank=True)#Email type
   created_date = models.DateTimeField(default=timezone.now())#Datetime
   description = models.TextField(blank=True) # text


