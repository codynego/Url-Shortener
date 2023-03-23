from django.shortcuts import render
from rest_framework.views import APIVIEW
from main.models import Urls
from serializers import UrlSerializer

# Create your views here.

class shorturl(APIVIEW):
    
	def get(self, request):
		urls = Urls.objects.all()
		serializer = UrlSerializer()


