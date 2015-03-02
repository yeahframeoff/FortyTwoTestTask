import datetime
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_func
from django.contrib.auth.forms import AuthenticationForm
from main.models import User, UserForm


def get_user():
    return User.objects.get(pk=1)


def mainpage(request):
    user = get_user()
    return render(request, 'mainpage.html', {'person': user})


@login_required
def editpage(request):
    user = get_user()
    if request.method == 'POST':
        if 'photo' in request.FILES:
            user.photo = request.FILES['photo']
            user.save()
            user.resize_photo()
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = UserForm(instance=user)
    return render(request, 'editpage.html', {'form': form})
