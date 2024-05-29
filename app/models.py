from django.db import models
from django import forms
from django.core.validators import *
def maximum_length_string(string):
    if len(string)<5:
        raise forms.ValidationError("Length must be greater than 5 ")
    
# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=20,primary_key=True,validators=[maximum_length_string])
    
    def __str__(self) -> str:
        return self.topic_name
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,validators=[MinLengthValidator(8)])
    email=models.EmailField()
    url=models.URLField()
    
    def __str__(self) -> str:
        return self.name
    
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=40)
    date=models.DateField()
    
    def __str__(self) -> str:
        return self.author