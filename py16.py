import mysql.connector as a
from mysql.connector import Error
conn=a.connect(host="localhost",user="root",password="root",database="place_tre")
mycu=conn.cursor()
sql="delete from customer where address='patna'"
#sql="select * from customer order by address"
#sql="select * from customer order by address"

mycu.execute(sql)
conn.commit()
print(mycu.rowcount,"deleted")
