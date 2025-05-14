# I have created this file - Mithun

from django.http import HttpResponse

def home(request):
    return HttpResponse('''<a href="https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F">Facebook</a>''')

def about(request):
    return HttpResponse('''<a href='https://www.instagram.com/#'>instagram</a>''')