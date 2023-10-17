from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from forms import RegisterForms


# Create your views here.

def login_view(request):
    form = AuthenticationForm()
    return render(request, 'my_django_project/login.html', {'form': form})


def admin_view(request):
    return render(request, 'my_django_project/admin.html')


def portfolio_view(request):
    return render(request, 'my_django_project/portfolio.html')


def register_view(request):
    form = RegisterForms()
    return render(request, 'my_django_project/register.html', {'form': form})
