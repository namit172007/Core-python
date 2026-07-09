from UserModel import UserModel
import datetime


def test_add():
    params = {}
    params['first_name'] = 'Namit'
    params['last_name'] = 'Rathi'
    params['login_id'] = 'anmitrathi@gmail.com'
    params['password'] = '123456'
    params['dob'] = datetime.date(2007, 4, 17)
    params['address'] = 'Indore'

    model = UserModel()
    try:
        model.add(params)
    except Exception as e:
        print('exception:', e)


def test_update():
    params = {}
    params['first_name'] = 'Namit'
    params['last_name'] = 'Rathi'
    params['login_id'] = 'namitrathi@gmail.com'
    params['password'] = '1234'
    params['dob'] = datetime.date(2017, 4, 13)
    params['address'] = 'Indore'
    params['id'] = 1

    model = UserModel()
    try:
        model.update(params)
    except Exception as e:
        print('exception:', e)


# test_add()
test_update()