from django.db import models

# Create your models here.
class Account(models.Model):
    points = models.PositiveIntegerField(default=0)
    current_job = models.CharField(max_length=100)