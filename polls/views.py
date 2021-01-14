from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings


def index(request):

    if settings.DEBUG:
        # Do something
        return HttpResponse("Debug true, Hello, world. You're at the polls index!")
    else:
        return HttpResponse("Hello, world. You're at the polls index!")
