from django.shortcuts import render, redirect

from .services.user_service import UserService
from .utility.data_validator import DataValidator


# Create your views here.
def welcome(request):
    return render(request, "welcome.html")


def validate_signup(request):
    form_error = {}
    form_error['error'] = False
    if (DataValidator.is_null(request.POST.get("firstName", ''))):
        form_error['first_name'] = "FIRST NAME REQUIRED"
        form_error['error'] = True
    if (DataValidator.is_null(request.POST.get("lastName", ''))):
        form_error['last_name'] = "LAST NAME REQUIRED"
        form_error['error'] = True
    if (DataValidator.is_null(request.POST.get("loginId", ''))):
        form_error['login_id'] = "LOGIN ID REQUIRED"
        form_error['error'] = True
    if (DataValidator.is_null(request.POST.get("password", ''))):
        form_error['password'] = "PASSWORD REQUIRED"
        form_error['error'] = True
    if (DataValidator.is_null(request.POST.get("dob", ''))):
        form_error['dob'] = "DOB REQUIRED"
        form_error['error'] = True
    if (DataValidator.is_null(request.POST.get("address", ''))):
        form_error['address'] = "ADDRESS REQUIRED"
        form_error['error'] = True
    return form_error


def validate_signin(request):
    form_error = {}
    form_error['error'] = False
    if (DataValidator.is_null(request.POST.get("loginId", ''))):
        form_error['login_id'] = "LOGIN ID REQUIRED"
        form_error['error'] = True
    if (DataValidator.is_null(request.POST.get("password", ''))):
        form_error['password'] = "FIRST NAME REQUIRED"
        form_error['error'] = True
    return form_error


def signup(request):
    form = {}
    form['message'] = ''
    form['error'] = False
    form['input_error']={}
    if request.method == 'POST':
        form['first_name'] = request.POST.get('firstName')
        form['last_name'] = request.POST.get('lastName')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['dob'] = request.POST.get('dob')
        form['address'] = request.POST.get('address')
        form['input_error']=validate_signup(request)
        if not form['input_error']['error']:
            try:
                UserService().add(form)
                form['message'] = "STUDENT ADDED SUCCESSFULLY"
            except Exception as e:
                form['message'] = e
                form['error'] = True
    return render(request, "signup.html", {'form': form})


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
                request.session['first_name'] = user[0].get('first_name')
                form['message'] = "LOGIN SUCCESSFUL"
                return redirect('/student/welcome/')
            else:
                form['message'] = "LOGIN UNSUCCESSFUL"
                form['error'] = True
    return render(request, "signin.html", {'form': form})


def logout(request):
    request.session.flush()
    return redirect('/student/signin/')
