from django.http import HttpResponse
from django.shortcuts import render, redirect

from .service.user_service import UserService
from .utility.data_validator import DataValidator


def user_signup_validate(request):
    input_error = {}
    input_error['error'] = False
    if (DataValidator.is_null(request.POST.get("firstName", ''))):
        input_error['first_name'] = 'First Name is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("lastName", ''))):
        input_error['last_name'] = 'Last Name is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("loginId", ''))):
        input_error['login_id'] = 'Login ID is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("password", ''))):
        input_error['password'] = 'Password is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("dob", ''))):
        input_error['dob'] = 'DOB is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("address", ''))):
        input_error['address'] = 'Address is required'
        input_error['error'] = True
    return input_error


def user_signin_validate(request):
    input_error = {}
    input_error['error'] = False
    if (DataValidator.is_null(request.POST.get("loginId", ''))):
        input_error['login_id'] = 'Login ID is required'
        input_error['error'] = True
    if (DataValidator.is_null(request.POST.get("password", ''))):
        input_error['password'] = 'Password is required'
        input_error['error'] = True
    return input_error


def ors_test(request):
    return HttpResponse('<h1>ORS App Test</h1>')


def welcome(request):
    return render(request, 'welcome.html')


def user_signup(request):
    form = {}
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}

    if request.method == "POST":
        form['first_name'] = request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')

        form['input_error'] = user_signup_validate(request)

        if not form['input_error']['error']:
            try:
                UserService().add(form)
                form['message'] = 'User Registration Successfully...!!!'
                form['error'] = False
            except Exception as e:
                form['message'] = str(e)
                form['error'] = True

    return render(request, 'registration.html', {'form': form})


def user_signin(request):
    form = {}
    form['message'] = ''
    form['error'] = False

    if request.method == "POST":

        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')

        form['input_error'] = user_signin_validate(request)

        if not form['input_error']['error']:
            user_data = UserService().authenticate(form['login_id'], form['password'])

            if user_data:
                request.session['first_name'] = user_data[0].get('first_name')
                return redirect('/ors/welcome/')
            else:
                form['message'] = 'Login ID & Password Invalid'
                form['error'] = True

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    request.session.flush()
    return redirect('/ors/signin/')
