from django.shortcuts import render, redirect
from .service.user_service import UserService
from .utility.data_validator import DataValidator


# Create your views here.

def welcome(request):
    return render(request, "welcome.html")


def validate_signup(request):
    form_error = {}
    form_error['error'] = False
    if DataValidator.is_null(request.POST.get('Name', '')):
        form_error['name'] = "NAME FIELD REQUIRED"
        form_error['error'] = True
    if DataValidator.is_null(request.POST.get('Course', '')):
        form_error['course'] = "COURSE FIELD REQUIRED"
        form_error['error'] = True
    if DataValidator.is_null(request.POST.get('loginId', '')):
        form_error['login_id'] = "LOGIN ID FIELD REQUIRED"
        form_error['error'] = True
    if DataValidator.is_null(request.POST.get('password', '')):
        form_error['password'] = "PASSWORD FIELD REQUIRED"
        form_error['error'] = True
    if DataValidator.is_null(request.POST.get('joiningDate', '')):
        form_error['joining_date'] = "JOINING DATE FIELD REQUIRED"
        form_error['error'] = True
    if DataValidator.is_null(request.POST.get('address', '')):
        form_error['address'] = " ADDRESS FIELD REQUIRED"
        form_error['error'] = True
    return form_error


def signup(request):
    form = {}
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}
    if request.method == 'POST':
        form['name'] = request.POST.get('Name')
        form['course'] = request.POST.get('Course')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['joining_date'] = request.POST.get('joiningDate')
        form['address'] = request.POST.get('address')
        form['input_error'] = validate_signup(request)

        if not form['input_error']['error']:
            try:
                UserService().add(form)
                form['message'] = "TEACHER ADDED SUCCESSFULLY"
            except Exception as e:
                form['message'] = e
                form['error'] = True
    return render(request, "signup.html", {'form': form})


def validate_signin(request):
    form_error = {}
    form_error['error'] = False
    if DataValidator.is_null(request.POST.get('loginId', '')):
        form_error['login_id'] = "LOGIN ID FIELD REQUIRED"
        form_error['error'] = True
    if DataValidator.is_null(request.POST.get('password', '')):
        form_error['password'] = "PASSWORD FIELD REQUIRED"
        form_error['error'] = True
    return form_error


def signin(request):
    form = {}
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}
    if request.method == 'POST':
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['input_error'] = validate_signin(request)

        if not form['input_error']['error']:
            user = UserService().authenticate(form)
            if user:
                request.session['name'] = user[0].get("name")
                form['message'] = "LOGIN SUCCESSFUL"
                return redirect('/teacher/welcome')
            else:
                form['message'] = "LOGIN UNSUCCESSFUL"
                form['error'] = True
    return render(request, "signin.html", {'form': form})


def logout(request):
    request.session.flush()
    return redirect("/teacher/signin")
