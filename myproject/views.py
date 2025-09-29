# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):

    # return HttpResponse("Hello World")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("I am Ali I work at Mathnasium. I am a computer scientist")
    return render(request, 'about.html')
