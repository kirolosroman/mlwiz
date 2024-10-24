from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
import io
from channels.layers import get_channel_layer
# Create your views here.

def index(response):
    return HttpResponse("<h1>hello there </h1>")
def home(response):
    return render(response,"main/home.html",{"name":"home"})

def heartdisease(response):
    return render(response,"main/classification/heartdisease.html",{})
def tests(response):
    return render(response,"main/tests.html",{})

def cv(response):
    return render(response,"main/cv.html")

async def plots(request):
    return HttpResponse(request, content_type='image/png')