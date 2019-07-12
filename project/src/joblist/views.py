from django.shortcuts import render
from .models import Job
from .forms import ImageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def jobs_list_view(request):
    jobs = Job.objects.all()
    jobs_dict = {
        'jobs': jobs
    }
    return render(request, "joblist/listjobs.html", jobs_dict)
    
def showImage(request):

    lastImage= Job.objects.last()

    imageFile= lastImage.imageFile


    form= ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'imagefile': imageFile,
              'form': form
              }
    
      
    return render(request, 'report/response.html', context)

