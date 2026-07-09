import pymysql

# Create Connection
connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='advance_python'
)

# Create Cursor
cursor = connection.cursor()


# ---------------- INSERT FUNCTIONS ---------------- #

def insert1():
    sql = "INSERT INTO marksheet VALUES (3,103,'raj',40,48,60)"
    cursor.execute(sql)
    connection.commit()
    print("DATA INSERTED PROPERLY")


def insert2():
    sql = "INSERT INTO marksheet VALUES (%s,%s,%s,%s,%s,%s)"
    data = (4, 104, 'namit', 40, 70, 50)
    cursor.execute(sql, data)
    connection.commit()
    print("DATA INSERTED PROPERLY")


def insert3(id, roll_no, name, phy, chem, maths):
    sql = "INSERT INTO marksheet VALUES (%s,%s,%s,%s,%s,%s)"
    data = (id, roll_no, name, phy, chem, maths)
    cursor.execute(sql, data)
    connection.commit()
    print("DATA INSERTED PROPERLY")


def insert4(data):
    id = data['id']
    roll_no = data['roll_no']
    name = data['name']
    phy = data['phy']
    chem = data['chem']
    maths = data['maths']

    sql = "INSERT INTO marksheet VALUES (%s,%s,%s,%s,%s,%s)"
    values = (id, roll_no, name, phy, chem, maths)

    cursor.execute(sql, values)
    connection.commit()
    print("DATA INSERTED PROPERLY")


# ---------------- UPDATE FUNCTIONS ---------------- #

def update1():
    sql = "UPDATE marksheet SET name='raj' WHERE id=4"
    cursor.execute(sql)
    connection.commit()
    print("DATA UPDATED PROPERLY")


def update2():
    sql = "UPDATE marksheet SET name=%s WHERE id=%s"
    data = ('namit', 5)

    cursor.execute(sql, data)
    connection.commit()
    print("DATA UPDATED PROPERLY")


def update3(id, name):
    sql = "UPDATE marksheet SET name=%s WHERE id=%s"
    data = (name, id)

    cursor.execute(sql, data)
    connection.commit()
    print("DATA UPDATED PROPERLY")


def update4(data):
    id = data['id']
    name = data['name']

    sql = "UPDATE marksheet SET name=%s WHERE id=%s"
    values = (name, id)

    cursor.execute(sql, values)
    connection.commit()
    print("DATA UPDATED PROPERLY")

def testDelete1():
    cursor = connection.cursor()
    sql = "delete from marksheet where id = 5"
    cursor.execute(sql)
    connection.commit()
    print('data deleted successfully')


def testDelete2():
    cursor = connection.cursor()
    sql = "delete from marksheet where id = %s"
    data = (8)
    cursor.execute(sql, data)
    connection.commit()
    print('data deleted successfully')


def testDelete3(id):
    cursor = connection.cursor()
    sql = "delete from marksheet where id = %s"
    data = (id)
    cursor.execute(sql, data)
    connection.commit()
    print('data deleted successfully')




# ---------------- FUNCTION CALLS ---------------- #

insert1()
insert2()
insert3(5, 105, 'dev', 48, 89, 78)

params = {
    'id': 6,
    'roll_no': 106,
    'name': 'abhi',
    'phy': 80,
    'chem': 80,
    'maths': 80
}

insert4(params)
update1()
update2()
update3(4, 'dev')

params_update = {
    'id': 5,
    'name': 'nidhi'
}

update4(params_update)

testDelete1()
testDelete2()
testDelete3(11)

# Close Connection
cursor.close()
connection.close()