import pymysql

class CollegeModel:
    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.close()
        return pk + 1


    def add(self, data):
        id = CollegeModel.next_pk(self)
        name = data.get('name','')
        address = data.get('address','')
        state=data.get('state','')
        city = data.get('city', '')
        phone_number = data.get('phone_number', '')

        college_exist = self.find_by_name(name)

        if len(college_exist) > 0:
            raise Exception('College already exist')

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "insert into college values (%s, %s, %s, %s, %s, %s)"
        data = (id,name,address,state,city,phone_number)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data.get('id',0)
        name = data.get('name','')
        address = data.get('address','')
        state=data.get('state','')
        city = data.get('city', '')
        phone_number = data.get('phone_number', '')

        college_exist = self.find_by_name(name)

        if len(college_exist) > 0 and college_exist[0].get('id')!=id :
            raise Exception('College already exist')

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "update college set name=%s, address=%s, state=%s, city=%s, phone_number=%s where id=%s"
        data = (name,address,state,city,phone_number,id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')


    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "delete from college where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def read(self):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select * from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "name", "address", "state", "city", "phone_number")
        res = []
        for x in result:
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def find_by_name(self, name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select * from college where name= %s"
        data = (name,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "name", "address", "state", "city", "phone_number")
        res = []
        for x in result:
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from college where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "name", "address", "state", "city", "phone_number")
        res = []
        for x in result:
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def search(self, data):
        name = data.get('name', '')
        address = data.get('address', '')
        state = data.get('state', '')
        city = data.get('city', '')
        phone_number = data.get('phone_number', '')
        page_size=data.get('page_size',0)
        page_number = data.get('page_number', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from college where 1=1"
        if name != '':
            sql += f" and name='{name}'"
        if address != '':
            sql += f" and address ='{address}'"
        if state != '':
            sql += f" and state='{state}'"
        if city != '':
            sql += f" and city ='{city}'"
        if phone_number != '':
            sql += f" and phone_number='{phone_number}'"
        if (page_size > 0):
            page_number = (page_number - 1) * page_size
            sql += " limit " + str(page_number) + ", " + str(page_size)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "name", "address", "state", "city", "phone_number")
        res = []
        for x in result:
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res