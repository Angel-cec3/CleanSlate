import uuid
from django.db import models

# Create your models here.
class Job(models.Model):
    location = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/', null=True, default=None)
    top_priority = models.BooleanField(default=False)
    job_id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)

    def __str__(self):
        return self.location
