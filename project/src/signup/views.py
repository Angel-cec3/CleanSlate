from django.shortcuts import render
from .models import userCreds, userCredsForm
from django.contrib.auth.models import User
# Create your views here.

def register_user(request):
    if request.method = 'POST':
        form = userCredsForm(request.POST)
        if form.is_valid():
            user_ = userCreds()
            user_.username = form.cleaned_data['username']
            user_.email = form.cleaned_data['email']
            user_.password = form.cleaned_data['password']
            user = User.objects.create_user(user_.username, user_.email, user_.password)
            user.save()
            return render(request, "home.html", {})
        return render(request, "home.html", {})




