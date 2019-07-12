from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(request.user)
        else:
            print('NAAAAYY')
        return render(request, "home.html", {})
    return render(request, "login/login.html", {})