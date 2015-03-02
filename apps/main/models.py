from __future__ import division

from django.db import models
from django.forms import ModelForm, Textarea
from PIL import Image


class User(models.Model):
    first_name = models.CharField(max_length=32, default='')
    last_name = models.CharField(max_length=32, default='')
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField(max_length=64, default='')
    jabber = models.CharField(max_length=64, null=True)
    skype = models.CharField(max_length=64, null=True)
    photo = models.ImageField(upload_to='user_photos', null=True)
    contacts = models.TextField(default='')

    RESIZE_TO = 200

    def resize_photo(self):
        if not self.photo:
            return

        image = Image.open(self.photo)
        width, height = image.size
        if width > height:
            factor = self.RESIZE_TO / height
        else:
            factor = self.RESIZE_TO / width
        size = (int(width * factor), int(height * factor))
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.photo.path)


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'bio': Textarea(attrs={'cols': 30, 'rows': 8}),
            'contacts': Textarea(attrs={'cols': 30, 'rows': 8})
        }
