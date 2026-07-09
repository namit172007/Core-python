from MarksheetModel import MarksheetModel


def test_add():
    params = {}
    # params['id'] = 8
    params['roll_no'] = 110
    params['name'] = 'abcde'
    params['physics'] = 80
    params['chemistry'] = 90
    params['maths'] = 79

    model = MarksheetModel()
    model.add(params)


def test_update():
    params = {}
    params['id'] = 3
    params['roll_no'] = 112
    params['name'] = 'ooo'
    params['physics'] = 70
    params['chemistry'] = 67
    params['maths'] = 79

    model = MarksheetModel()
    model.update(params)


def test_delete():
    model = MarksheetModel()
    model.delete(8)


def test_read():
    model = MarksheetModel()
    model.read()


def test_get():
    model = MarksheetModel()
    list = model.get(2)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',
              data['maths'], )


def test_find_by_rollno():
    model = MarksheetModel()
    list = model.find_by_roll(112)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',
              data['maths'], )


def test_search():
    params = {}
    # params['name'] = 'abc'
    # params['rollNo'] = 101
    params['page_no'] = 2
    params['page_size'] = 1
    model = MarksheetModel()
    list = model.search(params)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',
              data['maths'], )


# test_add()
# test_update()
# test_read()
# test_get()
# test_find_by_rollno()
test_search()