# docker run --name mysql_py_db -e MYSQL_ROOT_PASSWORD=root -d -p3306:3306 mysql
# docker exec -it mysql_py_db mysql -uroot -proot
import mysql.connector  

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root", database = "PythonDB2") 

#creating the cursor object  
cur = myconn.cursor()

try:
    #adding a column branch name to the table Employee  
    cur.execute("alter table Employee add branch_name varchar(20) not null")  
    
except:  
    print('rollback')
    myconn.rollback()
finally:
    print('connection closed')
    myconn.close()