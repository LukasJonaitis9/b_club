from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from . import forms

def signup(request:HttpRequest) -> HttpResponse:
    form = forms.CreateUserForm()
    return render(request, 'users/signup.html', {
        'form': form,
    })
