# I have created this file - Mithun

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Mithun")

def about(request):
    return HttpResponse("This is About Page")