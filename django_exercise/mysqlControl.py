import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1q2w3e', charset='utf8')
cursor = conn.cursor()

sql = "CREATE DATABASE mse"

cursor.execute(sql)

conn.commit()
conn.close()