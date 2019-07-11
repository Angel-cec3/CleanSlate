from django.shortcuts import render
from .models import Job

# Create your views here.
def jobs_list_view(request):
    obj = Job.objects.get(id=1)
    details = {
        'location': obj.location,
        'picture': obj.picture,
        'urgency': obj.urgency
    }
    return render(request, "joblist/listjobs.html", details)


