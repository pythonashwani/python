# append : add at the end of the file
#open the file.txt in write mode.    
fileptr = open("file2.txt","a")  
#overwriting the content of the file    
fileptr.write(" Python has an easy syntax and user-friendly interaction.")    
#closing the opened file     
fileptr.close()