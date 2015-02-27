from django.test import TestCase
from django.core.urlresolvers import reverse


# Create your tests here.
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
