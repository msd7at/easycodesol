from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def menu(request):
    res=render(request,"pythonds/pythondsmenu.html")
    return res
def w1q1(request):
    res=render(request,"pythonds/w1q1.html")
    return res
