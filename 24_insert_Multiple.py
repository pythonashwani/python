# docker run --name mysql_py_db -e MYSQL_ROOT_PASSWORD=root -d -p3306:3306 mysql
# docker exec -it mysql_py_db mysql -uroot -proot
import mysql.connector  

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root", database = "PythonDB2") 

#creating the cursor object  
cur = myconn.cursor()
sql = "insert into Employee(name, id, salary, dept_id, branch_name) values (%s, %s, %s, %s, %s)"  
#The row values are provided in the form of tuple   
val = [("John", 102, 25000.00, 201, "Newyork"),("David",103,25000.00,202,"Port of spain"),("Nick",104,90000.00,201,"Newyork")]
try:
    #inserting the values into the table  
    cur.executemany(sql,val) 
    print(cur.rowcount,"record inserted!")
    #commit the transaction   
    myconn.commit()

except:  
    print('rollback')
    myconn.rollback()
finally:
    print('connection closed')
    myconn.close()