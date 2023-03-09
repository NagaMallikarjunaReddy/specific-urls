from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('<h1>Dhoni is the best Finisher</h1>')

def abd(request):
    return HttpResponse('<h1> ABD is the monster</h1>')