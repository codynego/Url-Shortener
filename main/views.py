from django.shortcuts import render
import hashlib
import random
import string
from main.models import Url
from .forms import LinkForm

# Create your views here.
def hashurl(longurl):
    url = string.ascii_lowercase
    random_word = ''.join(random.choice(url) for i in range(8))
    longurl += random_word
    hashobj = hashlib.sha256(longurl.encode('utf-8'))
    hex_digit = hashobj.hexdigest()
    short_code = hex_digit[:8]
    return short_code 

    
def shorten(request):
    urls = Url.objects.all()
    if request.method == 'POST':
        if 
            

def redirect(request):
    if request.method == 'GET':
        



    
