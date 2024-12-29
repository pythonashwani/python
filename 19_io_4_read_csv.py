import csv  
with open('python.csv', newline = '') as csv_file:  
        csv_read = csv.reader( csv_file, delimiter = ',')  
        # To Read and display each row  
        for row in csv_read:  
            print(row)