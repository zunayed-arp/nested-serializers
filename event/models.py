from msilib.schema import CustomAction
from pyexpat import model
from tkinter import CASCADE
from django.db import models


class EventMain(models.Model):
    author = models.ForeignKey(related_name="user_events",on_delete=models.CASCADE)
    address_info= models.ForeignKey(related_name="event_address",on_delete=models.CASCADE)
    title = models.CharField(max_length=50,unique=True)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    max_seat = models.IntegerField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
def __str__(self):
    return self.title



class EventFeature(models.Model):
    eventmain = models.ForeignKey(related_name="event_features",on_delete=models.CASCADE)
    feature_name = models.DateTimeField(max_length=20)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.eventmain.title}-{self.feature_name}"
    
class EventAttender(models.Model):
    eventmain = models.ForeignKey(related_name="event_attender", on_delete=models.CASCADE)
    user = models.ForeignKey(,related_name="user_attendent",on_delete=models.CASCADE)
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.eventmain.title} - {self.user.name}"

    
