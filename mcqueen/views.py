from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    return HttpResponse('favas')

def head(request):
    return render(request, 'mcqueen\mc.html')

def mc(request):
    return render(request, 'mcqueen\mc2.html')   

