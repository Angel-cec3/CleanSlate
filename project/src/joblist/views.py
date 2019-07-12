from django.shortcuts import render
from .models import Job
from django.views.generic import ListView
from django.views.generic import ListView, CreateView 
from django.urls import reverse_lazy 

from .forms import PostForm 

# Create your views here.
def jobs_list_view(request):
    jobs = Job.objects.all()
    jobs_dict = {
        'jobs': jobs
    }
    return render(request, "joblist/listjobs.html", jobs_dict)


class HomePageView(ListView):
    model = Job
    template_name = 'joblist/listjobs.html'

class CreatePostView(CreateView): # new
    model = Job
    form_class = PostForm
    template_name = 'report/response.html'
    success_url = reverse_lazy('home')

