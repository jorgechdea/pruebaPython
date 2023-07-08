from django.db import models

# Create your models here.

class License(models.Model):
    companyName = models.CharField(max_length=100)
    userName = models.CharField(max_length=120)
    jobTitle = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    softwareUserName = models.CharField(max_length=100)
    expirationDate = models.DateField()
    version = models.CharField(max_length=50)