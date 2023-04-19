from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
from .models import *


def products(request):
    return HttpResponse('hi')
