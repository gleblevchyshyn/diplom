from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import User, Orderstatus


def products(request):

    return HttpResponse(Orderstatus.objects.all().values())
