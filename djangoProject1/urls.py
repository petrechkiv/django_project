"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from my_django_project import tests_views
from my_django_project.tests_views import login_view, base_view
from my_django_project.tests_views import portfolio_view
from my_django_project.tests_views import register_view

urlpatterns = [
    #path('login/', include('django.contrib.auth.urls')),
    #path('', base_view, name='base'),
    path('login/', login_view, name='login'),
    path('', login_view, name='login'),
    path('admin/', admin.site.urls),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('register/', register_view, name='register'),
]
