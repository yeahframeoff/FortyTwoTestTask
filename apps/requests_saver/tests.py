from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from requests_saver.models import RequestRecord


class HttpRequestDBSaveMiddlewareTest(TestCase):
    def test_record_is_saved_in_db_after_request(self):
        """
        After the request is done, it should be saved in database,
        and the search for RequestRecords should not return empty set.
        """
        time = timezone.now()
        self.client.get('/')
        request_entries = RequestRecord.objects.filter(time__gte=time)
        # Assert that list is not empty
        self.assertTrue(request_entries)

    def test_specified_page_contains_requests_history(self):
        """
        Following the request link we should see 10 recent requests.
        """
        for i in range(10):
            self.client.get(reverse('requests'))
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        requests = RequestRecord.objects.order_by('-time')[:10]
        requests = map(lambda x: '<RequestRecord: %s>' % x, requests)
        self.assertQuerysetEqual(response.context['recent_requests'], requests)
