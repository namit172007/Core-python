from Role import Role


def test_add():
    params = {}
    params['name'] = 'Nimitt'
    params['description'] = 'Student'
    model = Role()
    model.add(params)


def test_update():
    params = {}
    params['name'] = 'Namit'
    params['description'] = 'Btech Studnent'
    params['id']=2

    model = Role()
    model.update(params)


def test_delete():
    model = Role()
    model.delete(1)


def test_read():
    model = Role()
    list = model.read()
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'])

def test_get():
    model = Role()
    list = model.get(1)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'])


def test_find_by_name():
    model = Role()
    list = model.find_by_name('Namit')
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'])


def test_search():
    params = {}
    params['name'] = 'Namit'
    # params['description'] = 'Btech studnet'

    model = Role()
    list = model.search(params)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'])

# test_add()
# test_update()
# test_read()
# test_get()
# test_find_by_name()
test_search()