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

def user_list(request):
    form = {}
    form['page_no'] = 1
    form['page_size'] = 5
    form['list'] = []

    if request.method == "POST":
        if request.POST.get('operation', '') == "next":
            form['page_no'] = int(request.POST['pageNo'])
            form['page_no'] += 1
        if request.POST.get('operation', '') == "previous":
            form['page_no'] = int(request.POST['pageNo'])
            form['page_no'] -= 1
        if request.POST.get('operation', '') == "search":
            form['name'] = request.POST['Name']

    user_service = UserService()
    user_list = user_service.search(form)
    form['list'] = user_list
    form['index'] = (form['page_no'] - 1) * form['page_size']
    form['has_previous'] = form['page_no'] == 1
    form['has_next'] = len(user_list) < 5

    return render(request, "userlist.html", {"form": form})

def user_save(request, id=0):
    form = {}
    form['id'] = 0
    form['message'] = ''
    form['error'] = False
    form['input_error'] = {}

    if request.method == "GET" and id > 0:
        user_service = UserService()
        user_data = user_service.get(id)
        form['id'] = user_data[0].get('id')
        form['name'] = user_data[0].get('name')
        form['course'] = user_data[0].get('course')
        form['login_id'] = user_data[0].get('login_id')
        form['password'] = user_data[0].get('password')
        form['joining_date'] = user_data[0].get('joining_date').strftime('%Y-%m-%d')
        form['address'] = user_data[0].get('address')

    if request.method == "POST":
        if request.POST.get('operation', '') == "reset":
            return redirect('/teacher/save/')
        if request.POST.get('operation', '') == "list":
            return redirect('/teacher/list/')

    if request.method == "POST":
        form['id'] = int(request.POST.get('id', 0))
        form['name'] = request.POST.get('Name')
        form['course'] = request.POST.get('Course')
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        form['joining_date'] = request.POST.get('joiningDate')
        form['address'] = request.POST.get('address')

        form['input_error'] = validate_signup(request)

        if not form['input_error']['error']:
            user_service = UserService()
            try:
                if form['id'] > 0:
                    user_service.update(form)
                    form['message'] = 'User Updated Successfully...!!!'
                    form['error'] = False
                else:
                    user_service.add(form)
                    form['message'] = 'User Added Successfully...!!!'
                    form['error'] = False
            except Exception as e:
                form['message'] = e
                form['error'] = True

    return render(request, 'user.html', {'form': form})

def delete_user(request, id=0):
    UserService().delete(id)
    return redirect('/teacher/list/')

