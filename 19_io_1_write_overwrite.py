file = open('file.txt','w')  
file.write("Here we write a command")  
file.write("Hello users of Python")  
file.close()

#opens the file file.txt in read mode    
file = open("file.txt","r")    
if file:    
    print("file is opened successfully")   
#closes the opened file    
content = file.read();  
print(content)
file.close()