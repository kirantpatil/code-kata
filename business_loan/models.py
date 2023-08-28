from django.db import models
from django.utils import timezone


# Create your models here.
class Company(models.Model):  
    name = models.CharField(max_length=255)
    incorporation_year = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class Accounting_Provider(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name