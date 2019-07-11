from django.db import models
from django import forms

# Create your models here.
class userCreds(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

class userCredsForm(forms.ModelForm):
    class Meta:
        model = userCreds
        fields = [ 'username', 'email', 'password' ]
        widgets = {
            'password': forms.PasswordInput(),
        }
