from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from .forms import RegisterForms


# Create your views here.

def login_view(request, form=None, user_is_authenticated=None):
    tmpl_login = 'my_django_project/login.html'
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not login or not password:
            error = {'error': 'Введите имя пользователя и пароль'}
            return render(request, tmpl_login, {'error': error})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('portfolio')
        else:
            return render(request, 'error_auth.html', {'x': 'Ошибка!'})
    else:
        return render(request, tmpl_login, {'form': form})


def admin_view(request):
    return render(request, 'my_django_project/admin.html')


def portfolio_view(request):
    return render(request, 'my_django_project/portfolio.html')


def register_view(request):
    form = RegisterForms()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # проверка наличия логина в базе данных
        if User.objects.filter(username=username).exists():
            error = 'Пользователь с таким именем уже существует'
            return render(request, 'error.html', {'error': error})

        # добавление нового пользователя в базу данных
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # перенаправление пользователя на страницу входа
        return redirect('login')
    else:
        return render(request, 'my_django_project/register.html', {'form': form})
    # return render(request, 'my_django_project/register.html', {'form': form})


def base_view(request):
    return render(request, 'my_django_project/base.html')
