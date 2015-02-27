from requests_saver.models import RequestRecord


class RequestDBSaverMiddleware(object):
    def process_request(self, request):
        record = RequestRecord()
        record.method = request.method
        record.client_ip = request.META['REMOTE_ADDR']
        record.url = request.META['PATH_INFO']
        record.save()
        return None
