from rest_framework import serializer
from main.models import Url, AnalyticsEvent


class UrlSerializer(serializer.ModelSerializer):
    class Meta:
        model = Url
        fields = (user, longurl, shorturl, created_at, custom)