from django.http import HttpResponse
from django.shortcuts import render


def index(requet):
    return HttpResponse ("Hola mundo")

# Create your views here.
