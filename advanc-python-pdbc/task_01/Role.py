import pymysql

class Role:
    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from role"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.close()
        return pk + 1


    def add(self, data):
        id = Role.next_pk(self)
        name = data.get('name','')
        description = data.get('description','')

        role_exist = self.find_by_name(name)

        if len(role_exist) > 0:
            raise Exception('Role already exist')

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "insert into role values (%s, %s, %s)"
        data = (id,name,description)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        id = data.get('id',0)
        name = data.get('name', '')
        description = data.get('description', '')

        role_exist = self.find_by_name(name)

        if len(role_exist) > 0 and role_exist[0].get('id')!=id :
            raise Exception('Role already exist')

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "update role set name=%s, description=%s where id=%s"
        data = (name,description,id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')


    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "delete from role where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def read(self):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from role"
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "name", "description")
        res = []
        for x in result:
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def find_by_name(self, name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select * from role where name= %s"
        data = (name,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "name", "description")
        res = []
        for x in result:
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from role where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "name", "description")
        res = []
        for x in result:
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res

    def search(self, data):
        name = data.get('name', '')
        description = data.get('description', '')
        page_size=data.get('page_size',0)
        page_number = data.get('page_number', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from role where 1=1"
        if name != '':
            sql += f" and name='{name}'"
        if description != '':
            sql += f" and description ='{description}'"
        if (page_size > 0):
            page_number = (page_number - 1) * page_size
            sql += " limit " + str(page_number) + ", " + str(page_size)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "name", "description")
        res = []
        for x in result:
            res.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return res