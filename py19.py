import mysql.connector as a
from mysql.connector import Error
conn=a.connect(host="localhost",user="root",password="root",database="place_tre")
mycu=conn.cursor()
qu1="select min(id) from customer"
mycu.execute(qu1)
lo=mycu.fecthall()
print("id",lo)
conn.commit()
print(mycu.rowcount,"updated")

   
