import mysql.connector as a
from mysql.connector import Error
conn=a.connect(host="localhost",user="root",password="root",database="place_tre")
if conn.is_connected():
    print("Succes")
else:
    print("fail")

mycu=conn.cursor()
sql="insert into customer (name,address)values(%s,%s)"
val=("Raviji","Patna")
mycu.execute(sql,val)
conn.commit()
print(mycu.lastrowid,"1 Record was inserted")