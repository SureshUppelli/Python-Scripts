import pymysql
conn = pymysql.connect(host='localhost', user='root', password='Novi1234', db='mysql')
a = conn.cursor()
sql = 'SELECT * from `user`;'
a.execute(sql)
countrow = a.execute(sql)
print("Number of rows :", countrow)
data = a.fetchone()
print (data)
