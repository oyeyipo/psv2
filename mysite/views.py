from django.shortcuts import render
from django.http import HttpResponse


def landing_page(request):
    return HttpResponse("<html><title>Oyeyipo Olawale</title></html>")
