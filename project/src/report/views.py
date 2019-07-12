from django.shortcuts import render
from joblist.models import Job

# Create your views here.
def report_place(request):
	return render(request, "report/response.html", {})