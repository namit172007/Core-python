from CollegeModel import CollegeModel


def test_add():
    params = {}
    params['name'] = 'Nisha'
    params['address'] = 'Indore'
    params['state'] = 'MP'
    params['city'] = 'Indore'
    params['phone_number'] = '9980898909'

    model = CollegeModel()
    model.add(params)


def test_update():
    params = {}
    params['name'] = 'Namit'
    params['address'] = 'Bengaluru'
    params['state'] = 'Karnatka'
    params['city'] = 'Bengaluru'
    params['phone_number'] = '9898986789'
    params['id']=1

    model = CollegeModel()
    model.update(params)


def test_delete():
    model = CollegeModel()
    model.delete(1)


def test_read():
    model = CollegeModel()
    list = model.read()
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'],
              '\t',data['phone_number'])

def test_get():
    model = CollegeModel()
    list = model.get(1)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'],
              '\t', data['phone_number'])


def test_find_by_name():
    model = CollegeModel()
    list = model.find_by_name('Namit')
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'],
              '\t', data['phone_number'])


def test_search():
    params = {}
    # params['name'] = 'Namit'
    params['address'] = 'Indore'
    # params['state'] = 'MP'
    # params['city'] = 'Indore'
    # params['phone_number'] = 9898986789
    model = CollegeModel()
    list = model.search(params)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'],
              '\t', data['phone_number'])


# test_add()
# test_update()
# test_read()
# test_get()
# test_find_by_name()
test_search()