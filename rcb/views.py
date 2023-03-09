from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<h2> <marquee>virat is the best batsman in the world</marquee><h2>')

def sharma(request):
    return HttpResponse("<h2><marquee> virat is anushkasharma's husband</marquee></h2>")