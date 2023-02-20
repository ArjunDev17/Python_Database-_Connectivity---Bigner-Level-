import mysql.connector as a
from mysql.connector import Error
conn=a.connect(host="localhost",user="root",password="root",database="place_tre")
mycu=conn.cursor()
sql="select *from customer where address=%s"
adr=("patna",)
mycu.execute(sql,adr)
myRe=mycu.fetchall()
for x in myRe:
    print(x)