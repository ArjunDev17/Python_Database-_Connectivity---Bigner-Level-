import mysql.connector as a
from mysql.connector import Error
conn=a.connect(host="localhost",user="root",password="root",database="place_tre")
if conn.is_connected():
    print("Succes")
else:
    print("fail")

mycu=conn.cursor()
sql="insert into customer (name,address)values(%s,%s)"

mycu.execute("select name,address from customer" )
myR=mycu.fetchone()
for x in myR:
    print(x)
#print(mycu.rowcount,"Record was inserted")