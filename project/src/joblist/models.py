from django.db import models
from django import forms

# Create your models here.
class Job(models.Model):
    location = models.CharField(max_length=100)
    picture = models.FileField(upload_to='images/', null=True, verbose_name="")
    top_priority = models.BooleanField(default=False)

    def __str__(self):
        return self.location + ": " + str(self.picture) + ":" + self.top_priority
