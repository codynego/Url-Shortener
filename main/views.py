from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
import hashlib
import random
import string
from main.models import Url
from .forms import LinkForm


# Create your views here.


def hash_url(longurl):
    url = string.ascii_lowercase
    random_word = ''.join(random.choice(url) for i in range(8))
    longurl += random_word
    hashobj = hashlib.sha256(longurl.encode('utf-8'))
    hex_digit = hashobj.hexdigest()
    short_code = hex_digit[:8]
    return short_code


def home(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.valid():
            longurl = form.cleaned_data['longurl']
            shorturl = hash_url(longurl)
            link = Url(longurl=longurl, shorturl=shorturl)
            link.save()
            context = {
                'shorturl': shorturl,
            }
            return render(request, 'home.html', context)
    form = LinkForm()
    context = {
        'form': form,
    }
    return render(request, 'home.html', context)


def redirect_url(request, shorturl):
    try:
        url = get_object_or_404(Url, short_url=shorturl)
        return redirect(url.long_url)
    except Url.DoesNotExist:
        return HttpResponseNotFound('Short URL not found')
