from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import PageCount

# Create your views here.

def index(request):
    row, create = PageCount.objects.get_or_create(page='index')
    row.count += 1
    row.save()
    
    return HttpResponse("Hello,  at visitor #"+ str(row.count) + " " + time.strftime('%c'))
    #visitor #"+ str(row.count) + "
    