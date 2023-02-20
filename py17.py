import mysql.connector as a
from mysql.connector import Error
conn=a.connect(host="localhost",user="root",password="root",database="place_tre")
mycu=conn.cursor()
sql="update customer set address='Gya' where address='mp'"


mycu.execute(sql)
conn.commit()
print(mycu.rowcount,"updated")

