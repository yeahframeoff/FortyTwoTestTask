import datetime
from django.shortcuts import render
from main.models import User, Contact


def mainpage(request):
    user = User.objects.get(pk=1)
    return render(request, 'mainpage.html', {'user': user})
