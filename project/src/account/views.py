from django.shortcuts import render
from .forms import AccountForm
from .models import Account
# Create your views here.

def account_summary_view(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid:
            obj = Account()
            obj.current_job = request.POST['current_job']
            obj.save()
            return render(request, "home.html", {})
    else:
        form = AccountForm()
    return render(request, "account/account.html", { 'form': form})
