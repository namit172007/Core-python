from django.http import HttpResponse
from django.shortcuts import render


def test_ors(request):
    return HttpResponse("<h1>Hello Th is is Django Project in orssss</h1>")

def user_signup(request):
    return render(request, 'UserRegistration.html')
def welcome(request):
    return render(request,'Welcome.html')

