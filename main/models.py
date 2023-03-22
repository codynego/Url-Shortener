from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    longurl = models.CharField(max_length=100)
    shorturl = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    custom = models.CharField(max_length=50, Null=True)


class AnalyticsEvent(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
    page_url = models.URLField(max_length=200)
    device_type = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    referrer = models.URLField(max_length=200)
    outcome = models.CharField(max_length=50)
