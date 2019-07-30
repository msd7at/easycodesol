from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    res=render(request,"joc/jocmenu.html")
    return res
def week1quiz(request):
    res=render(request,"joc/w1quiz.html")
    return res
