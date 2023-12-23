# docker run --name mysql_py_db -e MYSQL_ROOT_PASSWORD=root -d -p3306:3306 mysql
# docker exec -it mysql_py_db mysql -uroot -proot
import mysql.connector  

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root", database = "PythonDB2") 

#creating the cursor object  
cur = myconn.cursor()
try:
    #updating the name of the employee whose id is 110  
    cur.execute("update Employee set name = 'alex' where id = 110")  
    # Deleting the employee details whose id is 110  
    # cur.execute("delete from Employee where id = 110")  
except:  
    print('rollback')
    myconn.rollback()
finally:
    print('connection closed')
    myconn.close()