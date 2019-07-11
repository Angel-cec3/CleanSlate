from django.db import models
from django import forms

# Create your models here.
class Job(models.Model):
    location = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    top_priority = models.BooleanField(default=False)

class JobForm(forms.Form):
    location = forms.CharField(max_length=100)
    picture = forms.CharField(max_length=100)
    top_priority = forms.BooleanField(required=False)

