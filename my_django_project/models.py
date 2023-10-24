from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile1(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #name = models.CharField(max_length=20)
    #description = models.TextField()
    #technology = models.CharField(max_length=50)
