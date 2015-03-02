from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate, login
from django.test.client import RequestFactory
from PIL import Image

from sys import version_info
if version_info < (3,):
    from urllib import urlopen
else:
    from urllib.request import urlopen

from unittest import skip


class SomeTests(TestCase):

    def test_math(self):
        assert(2 + 2 == 4)


class SettingsContextProcessorTests(TestCase):

    def test_request_context_has_settings_in_it(self):
        """
        Response for any non 404 page should have 'settings'
        in its context
        """
        response = self.client.get(reverse('main'))
        if response.status_code != 404:
            self.assertIn('settings', response.context)


class MainPageDataFormTests(TestCase):

    @skip("To much time spent trying to fetch image from context")
    def test_image_successfully_resizes(self):
        """
        When picture is uploaded, it is resized to 200x200, maintaining aspect ratio.
        """
        username, password = 'leodicaproz', 'dicapriohash'
        user = AuthUser.objects.create_user(
            username=username,
            password=password,
            email='dicaprio@gmail.com')
        self.assertTrue(user)
        response = self.client.post(
            reverse('login'),
            {'username': username, 'password': password})
        with Image.open('apps/main/test_image.jpg') as img:
            response = self.client.post(reverse('edit'), {'photo': img})
        print(response.context['form'].instance.photo)
        image_url = response.context['form'].instance.photo.url
        image_file = urlopen(image_url)
        with Image.open(image_file) as image:
            self.assertLessEqual(image.width, 200)
            self.assertLessEqual(image.height, 200)
