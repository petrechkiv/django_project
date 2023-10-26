from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserModel
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import RegisterForms


# Create your views here.

def login_view(request, form=None, user_is_authenticated=None):
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # обработка введенных данных пользователя
        if not username or not password:
            context = {'error': 'Введите имя пользователя и пароль'}
            return render(request, 'my_django_project/login.html', {'form': form})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # проверка наличия пользователя в базе данных
            if user.is_active:
                login(request, user)
                return redirect('portfolio')
            else:
                #context = {'error': 'Данный пользователь заблокирован'}
                error = 'Пользователь заблокирован'
                return render(request, 'my_django_project/login.html', {'error': error})
        else:
            #context = {'error': 'Неверное имя пользователя или пароль'}
            error = 'Неверное имя пользователя или пароль'
            return render(request, 'my_django_project/login.html', {'error':error})
    else:
        return render(request, 'my_django_project/login.html', {'form': form})


def admin_view(request):
    return render(request, 'my_django_project/admin.html')


def portfolio_view(request):
    return render(request, 'my_django_project/portfolio.html')


def register_view(request):
    form = RegisterForms()
    return render(request, 'my_django_project/register.html', {'form': form})


def base_view(request):
    return render(request, 'my_django_project/base.html')
