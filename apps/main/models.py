from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=32, default='')
    last_name = models.CharField(max_length=32, default='')
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.CharField(max_length=64, default='')
    jabber = models.CharField(max_length=64, default='')
    skype = models.CharField(max_length=64, default='')


class Contact(models.Model):
    user = models.ForeignKey(User)
    contact_type = models.CharField(max_length=20)
    value = models.CharField(max_length=64)
