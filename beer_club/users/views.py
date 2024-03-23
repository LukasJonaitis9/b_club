from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from . import forms

def signup(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form= forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Thank you! You successfully joined BeerClub."))
            return redirect('login')
    else:
        form = forms.CreateUserForm()
    return render(request, 'users/signup.html', {
        'form': form,
    })
