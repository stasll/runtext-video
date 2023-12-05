from django.db import models

# Create your models here.
class RequestLog(models.Model):
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField()