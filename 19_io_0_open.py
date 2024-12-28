#opens the file file.txt in read mode    
file = open("file.txt","r")    
if file:    
    print("file is opened successfully")   
#closes the opened file    
content = file.read();  
print(content)
file.close()