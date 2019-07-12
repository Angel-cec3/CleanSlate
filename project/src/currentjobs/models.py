from django.db import models
from joblist.models import Job

# Create your models here.
class Task(Job, models.Model):
    completed = models.BooleanField(default=False)
