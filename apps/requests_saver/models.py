from django.utils import timezone
from django.db import models

class RequestRecord(models.Model):
    time = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=256)
    method = models.CharField(max_length=10)
    client_ip = models.CharField(max_length=16)

    def __str__(self):
        return '%s: %s -> %s %s' % (self.client_ip, self.time, self.method, self.url)