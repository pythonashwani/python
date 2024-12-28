# open the file.txt in append mode. Create a new file if no such file exists.  
fileptr = open("file2.txt", "w")  
# appending the content to the file  
fileptr.write('''Python is the modern programming language. It is done any kind of program in shortest way.''')  
# closing the opened the file  
fileptr.close()  