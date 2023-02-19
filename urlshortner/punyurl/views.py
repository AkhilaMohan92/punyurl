from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from random import choice
from .forms import UrlForm
from .models import Shortner
import string
from . import constants
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def generate_short_id(request):
    if request.method == 'POST':
        s = Shortner()
        form = UrlForm(request.POST)
        if form.is_valid():
            s.url = form.cleaned_data['url']
            validate_url = URLValidator()
            try:
                validate_url(s.url)
            except ValidationError as e:
                return render(request, 'short_url.html', {'error':constants.INVALID_URL})

        """
        Generate short_id 8 characters. 
        Can be modified in future to accept number of characters from user
        """
        s.shorturl = ''.join(choice(string.ascii_letters+string.digits) for _ in range(8))
        s.save()
        tgt_url = constants.BASE_URL + s.shorturl

        return render(request, 'short_url.html', {'text':constants.URL_TEXT,'url':tgt_url})


def find_url(request,shorturl):

    if request.method == 'GET':
        longurl = Shortner.objects.filter(shorturl=shorturl).values()[0]
        return HttpResponseRedirect(longurl['url'])


def index(request):

    form = UrlForm()

    return render(request, 'url.html', {'form': form})
