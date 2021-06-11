from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)

class user_cps(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)

class Ride(models.Model):
    name = models.CharField(max_length=122)
    source = models.CharField(max_length=122)
    destination = models.CharField(max_length=122)
    car = models.CharField(max_length=122)
    contact = models.CharField(max_length=100)
    
    class Meta:
        db_table = "ride"
    



