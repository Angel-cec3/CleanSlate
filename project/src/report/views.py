from django.shortcuts import render
from joblist.models import Job, JobForm

# Create your views here.
def report_place(request):
	if request.method == 'POST':
		form = JobForm(request.POST)
		if form.is_valid():
			job = Job()
			job.location = form.cleaned_data['location']
			job.picture = form.cleaned_data['picture']
			job.top_priority = form.cleaned_data['top_priority']
			job.save()
			return render(request, "home.html", {})
	else:
		form = JobForm()

	return render(request, "report/response.html", { 'form': form })