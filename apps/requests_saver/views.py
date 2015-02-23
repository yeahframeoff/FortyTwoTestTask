from django.shortcuts import render
from requests_saver.models import RequestRecord

def requestspage(request):
    requests = RequestRecord.objects.order_by('-time')[:10]
    context = {'recent_requests': requests}
    return render(request, 'index.html', context)