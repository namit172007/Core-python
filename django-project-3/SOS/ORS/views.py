from django.shortcuts import render, redirect


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    message = ''

    if request.method == "POST":
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        login_id = request.POST.get('loginId')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        address = request.POST.get('address')

        if first_name != '' and last_name != '' and login_id != '' and password != '':
            message = 'User Registration Successfully...!!!'
        else:
            message='Not All Fields Filled'

    return render(request, 'registration.html', {'message': message})


def user_signin(request):
    message = ''

    if request.method == "POST":
        login_id = request.POST.get('loginId')
        password = request.POST.get('password')
        if login_id == 'admin' and password == 'admin':
            return render(request, 'welcome.html', {'name': 'Admin'})
        else:
            message = 'Login ID & Password Invalid'

    return render(request, 'login.html', {'message': message})


def test_list(request):
    list = [
        {"id": 1, "firstName": "abc", "lastName": "xyz", "email": "abc@gmail.com", "password": "12345"},
        {"id": 2, "firstName": "pqr", "lastName": "pqr", "email": "pqr@gmail.com", "password": "12345"},
        {"id": 3, "firstName": "klm", "lastName": "klm", "email": "klm@gmail.com", "password": "12345"}
    ]
    return render(request, "testlist.html", {"list": list})




# Create your views here.
