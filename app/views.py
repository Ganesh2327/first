from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def p1(request):
    return HttpResponse('<B><marquee><h>HIIIIIII</h></marquee></B')


def p2 (request):
    return HttpResponse('<h1><marquee><B>Hello</B></marquee></h1>')

def p3(request):
    return HttpResponse('<marquee><h1><B>GANESH</marquee></h1></B>')
