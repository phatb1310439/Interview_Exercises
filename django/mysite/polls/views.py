from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    #part 1
    response = HttpResponse()
    response.writelines("<h1>HELLO DJANGO<h1>")
    response.writelines("<h2>My name's Phat<h2>")
    response.writelines("<h3>You're at the polls index<h3>")
    return response