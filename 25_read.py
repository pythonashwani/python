# docker run --name mysql_py_db -e MYSQL_ROOT_PASSWORD=root -d -p3306:3306 mysql
# docker exec -it mysql_py_db mysql -uroot -proot
import mysql.connector  

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root", database = "PythonDB2") 

#creating the cursor object  
cur = myconn.cursor()
try:
    #Reading the Employee data      
    cur.execute("select * from Employee")  
 
    #fetching the rows from the cursor object  
    result = cur.fetchall()  

    #printing the result
    for x in result:  
        print(x);  

    

except:  
    print('rollback')
    myconn.rollback()
finally:
    print('connection closed')
    myconn.close()

''''
    1. Reading the Employee data -  names that start with j     
    cur.execute("select name, id, salary from Employee where name like 'J%'")  
    2. Reading the Employee data - names with id = 101, 102, and 103
    cur.execute("select name, id, salary from Employee where id in (101,102,103)")  
    3. Order by desc (if not specify then asc)
    cur.execute("select name, id, salary from Employee order by name desc") 

    4. fetching the first row from the cursor object  
    result = cur.fetchone() 

    5. printing the result in format  
    print("Name    id    Salary");  
    for row in result:  
        print("%s    %d    %d"%(row[0],row[1],row[2]))  

'''