from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'Welcome.html')
def signup(request):
    return render(request,'SignUp.html')

