from django.db import connection


class UserService:

    def next_pk(self):
        pk = 0
        cursor = connection.cursor()
        sql = "select max(id) from sos_user2"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.close()
        return pk + 1

    def add(self, data):
        id = UserService.next_pk(self)
        name = data['name']
        course = data['course']
        login_id = data['login_id']
        password = data['password']
        joining_date = data['joining_date']
        address = data['address']

        user_exist = self.find_by_login(login_id)

        if len(user_exist) > 0:
            raise Exception('Login ID already exist')

        cursor = connection.cursor()
        sql = "insert into sos_user2 values(%s, %s, %s, %s, %s, %s, %s)"
        data = (id, name, course, login_id, password, joining_date , address)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        # id = UserService.next_pk(self)
        id = data['id']
        name = data['name']
        course = data['course']
        login_id = data['login_id']
        password = data['password']
        joining_date = data['joining_date']
        address = data['address']

        user_exist = self.find_by_login(login_id)

        if len(user_exist) > 0 and user_exist[0].get('id') != id:
            raise Exception('Login ID already exist')

        cursor = connection.cursor()
        sql = "update sos_user2 set name = %s, course = %s,login_id = %s, password = %s, joining_date = %s, address = %s where id = %s"
        data = ( name, course, login_id, password, joining_date , address,id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')

    def delete(self, id):
        cursor = connection.cursor()
        sql = "delete from sos_user2 where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def get(self, id):
        cursor = connection.cursor()
        sql = "select * from sos_user2 where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ('id', 'name', 'course', 'login_id', 'password', 'joining_date' , 'address')
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def find_by_login(self, login_id):
        cursor = connection.cursor()
        sql = "select * from sos_user2 where login_id = %s"
        data = (login_id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ('id', 'name', 'course', 'login_id', 'password', 'joining_date' , 'address')
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def authenticate(self, data):
        cursor = connection.cursor()
        login_id=data['login_id']
        password= data['password']
        sql = "select * from sos_user2 where login_id = %s and password = %s"
        data = (login_id,password)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ('id', 'name', 'course', 'login_id', 'password', 'joining_date' , 'address')
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def search(self, params):
        name = params.get('name', '')
        joinging_date = params.get('course', 0)
        page_no = params.get('page_no', 0)
        page_size = params.get('page_size', 0)
        cursor = connection.cursor()
        sql = "select * from sos_user2 where 1=1"
        if name != '':
            sql += " and first_name like '" + name + "%%'"
        if joinging_date != 0:
            sql += " and dob = " + str(joinging_date)
        if (page_size > 0):
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ('id', 'name', 'course', 'login_id', 'password', 'joining_date' , 'address')
        res = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res