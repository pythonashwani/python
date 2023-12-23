# docker run --name mysql_py_db -e MYSQL_ROOT_PASSWORD=root -d -p3306:3306 mysql
# docker exec -it mysql_py_db mysql -uroot -proot
import mysql.connector  

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root") 

#creating the cursor object  
cur = myconn.cursor()

try:
    #creating a new database
    cur.execute("create database PythonDB2")
    #getting the list of all the databases which will now include the new database PythonDB
    dbs = cur.execute("show databases")
    for x in cur:
        print(x)
except:  
    myconn.rollback()
finally:
    myconn.close()