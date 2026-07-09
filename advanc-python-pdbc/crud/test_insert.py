import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
cursor = connection.cursor()
sql = "insert into marksheet values(2, 102, 'raj', 14, 60, 48)"
cursor.execute(sql)
connection.commit()
connection.close()
print('data inserted successfully')