from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserModel
from django.contrib.auth.models import User
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
        diclog = dict()
        if not login or not password:
            error = {'error': 'Введите имя пользователя и пароль'}
            return render(request, 'my_django_project/login.html', {'error': error})

        for i in UserModel.objects.all():
            diclog[i.username] = i.password

        if login in diclog.keys() and password == diclog[login]:
            return redirect('portfolio')
        else:
            return render(request, 'Error_aut.html', {'x': 'Ошибка!'})
    else:
        return render(request, 'my_django_project/login.html', {'form': form})
    #
    #
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #
    #     # обработка введенных данных пользователя
    #     if not username or not password:
    #         context = {'error': 'Введите имя пользователя и пароль'}
    #         return render(request, 'my_django_project/login.html', {'form': form})
    #
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         # проверка наличия пользователя в базе данных
    #         if user.is_active:
    #             login(request, user)
    #             return redirect('portfolio')
    #         else:
    #             # context = {'error': 'Данный пользователь заблокирован'}
    #             error = 'Пользователь заблокирован'
    #             return render(request, 'my_django_project/login.html', {'error': error})
    #     else:
    #         # context = {'error': 'Неверное имя пользователя или пароль'}
    #         error = 'Неверное имя пользователя или пароль'
    #         return render(request, 'my_django_project/login.html', {'error': error})
    # else:
    #     return render(request, 'my_django_project/login.html', {'form': form})


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
            return render(request, 'my_django_project/register.html', {'error': error})

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

# def reg(request):  # Регистрация пользователя
#     if request.method == 'POST':
#         # обработка POST запроса
#         l = request.POST['login']
#         p = request.POST['pas']
#         e = request.POST['email']
#         n = UserModel()
#         arrlog = []
#         arrpas = []
#         for i in UserModel.objects.all():  # прохождение по всме записям модели UserModel
#             arrlog.append(i.log)  # Добавление логинов в список
#             arrpas.append(i.pas)  # Добавление паролей в список
#         if l in arrlog:  # Если такрй логин есть, то ошибка!
#             return render(request, 'Error.html')
#         n.log = l  # Если такого логина нет, то добавляем его в модель
#         n.pas = p
#         n.email = e
#         n.save()
#         # return render(request, 'New.html') # и отправляем на новую страницу
#         return redirect(f'/New?hello=Hello, {l}')  # передаем в адресную сторку
#     return render(request, 'Authorisation.html')


# def auth(request):
#     if request.method == 'POST':
#         l = request.POST['login']
#         p = request.POST['pas']
#         diclog = dict()
#
#         for i in UserModel.objects.all():
#             diclog[i.log] = i.pas
#
#         if l in diclog.keys() and p == diclog[l]:
#             return redirect(f'/New?hello=Helloy, {l}')
#
#         else:
#             return render(request, 'Error_aut.html', {'x': 'Ошибка!'})
