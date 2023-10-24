from django import forms
from django.shortcuts import redirect


class RegisterForms(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    email = forms.EmailField(label='E-mail')


