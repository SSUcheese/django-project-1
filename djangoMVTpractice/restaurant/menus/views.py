from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
from menus.models import Menu
# Create your views here.
def greetings(request):
    return HttpResponse("<h2>hello world<h2/>")

def index(request):
    date = datetime.today().date()
    kind = Menu.objects.all()
    context = {}
    context['date'] = date
    context['kind'] = kind
    return render(request, 'menus/index.html', context=context)

def detail(request, menu):
    context = dict()
    context['name'] = menu
    return render(request, 'menus/detail.html', context= context)