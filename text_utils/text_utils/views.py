# I have created this file - Mithun

from django.http import HttpResponse

from django.shortcuts import render 

def index(request):
    params = {'name':'Mithun','age':27}
    return render(request,'index.html',params)
