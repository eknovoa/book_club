from django.http import HttpResponse
from django.template import loader

# Create your views here.

def books(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def database(request):
    template = loader.get_template('database.html')
    return HttpResponse(template.render())

def poll(request):
    template = loader.get_template('poll.html')
    return HttpResponse(template.render())
