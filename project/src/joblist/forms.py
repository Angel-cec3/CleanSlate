from django import forms
from .models import Job

class PostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['location', 'picture', 'top_priority']

