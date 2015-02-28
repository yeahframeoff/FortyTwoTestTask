from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.CharField(max_length=64)
    jabber = models.CharField(max_length=64)
    skype = models.CharField(max_length=64)


class Contact(models.Model):
    user = models.ForeignKey(User)
    contact_type = models.CharField(max_length=20)
    value = models.CharField(max_length=64)
