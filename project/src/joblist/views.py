from django.shortcuts import render
from .models import Job
from django.contrib.auth.decorators import login_required

# Create your views here.
def jobs_list_view(request):
    jobs = Job.objects.all()
    jobs_dict = {
        'jobs': jobs
    }
    return render(request, "joblist/listjobs.html", jobs_dict)
    


