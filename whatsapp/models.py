from email import message
from django.db import models

# Create your models here.

class Phone(models.Model):
    phone_number = models.CharField(max_length=12)
    message = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.phone_number