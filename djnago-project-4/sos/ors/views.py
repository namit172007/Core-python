from django.shortcuts import render
def welcome(request):
    return render(request,"Welcome.html")
def signup (request):
    return render(request,"SignUp.html")
def signin (request):
    return render(request,"SignIn.html")
