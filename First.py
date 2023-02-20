import mysql.connector as a
from mysql.connector import Error
conn=a.connect(host="localhost",user="root",password="root",database="place_tre")
if conn.is_connected():
    print("Succes")
else:
    print("fail")
mycu=conn.cursor()
mycu.execute("show databases")
for x in mycu:
    print(x)
mycu.execute("show tables")
print("tables")
for x in mycu:
    print(x)   
#mycu.execute("create table customer(name varchar(225),address varchar(255))")