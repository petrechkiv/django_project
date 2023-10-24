from django.contrib.auth.forms import AuthenticationForm, UserModel
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import RegisterForms


# Create your views here.
def portfolio_view(request):
    return redirect('/portfolio/')


def login_view(request, form=None):
    form = AuthenticationForm()
    return render(request, 'my_django_project/login.html', {'form': form})


def admin_view(request):
    return render(request, 'my_django_project/admin.html')


def redirect_to_portfolio_view(request):
    url = reverse('login_view')
    return redirect('/portfolio/')


def register_view(request):
    form = RegisterForms()
    return render(request, 'my_django_project/register.html', {'form': form})


def base_view(request):
    return render(request, 'my_django_project/base.html')
