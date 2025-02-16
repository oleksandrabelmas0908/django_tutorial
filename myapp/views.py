from django.shortcuts import render

from .models import Tour


def index(req):
    tours = Tour.objects.all()
    data = {'tours': tours}
    return render(req, 'index.html', data)
