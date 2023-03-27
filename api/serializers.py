from rest_framework import serializers
from main.models import Url, Analytics


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('longurl', 'shorturl')


class AnalyticSerializer(serializers.ModelSerializer):
    url = UrlSerializer()

    class Meta:
        model = Analytics
        fields = ('date_time', 'user_id', 'page_url', 'device_type', 'referrer', 'location','url')