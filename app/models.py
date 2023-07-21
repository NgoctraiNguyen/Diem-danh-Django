from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Staffs(models.Model):
    customer = models.ForeignKey(User, on_delete= models.SET_NULL, null= True)
    name = models.CharField(max_length=200, null=True)
    classroom = models.CharField(max_length=200, null=True)
    phonenumber = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.name)
    
class Event(models.Model):
    customer = models.ForeignKey(User, on_delete= models.SET_NULL, null= True)
    name = models.CharField(max_length=500, null=True)
    date = models.DateField(null=True)
    description = models.CharField(max_length=5000, null=True)

    def __str__(self):
        return str(self.name)
    
class Acttendence(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null= True)
    staff = models.ForeignKey(Staffs, on_delete=models.SET_NULL, null= True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.staff)