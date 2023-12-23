Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday","Tuesday","Sunday", "Friday"}    
print(Days1&Days2) #prints the intersection of the two sets    
set1 = {"Devansh","John", "David", "Martin"}    
set2 = {"Steve", "Milan", "David", "Martin"}    
print(set1.intersection(set2)) #prints the intersection of the two sets
set1 = {1,2,3,4,5,6,7}  
set2 = {1,2,20,32,5,9}  
set3 = set1.intersection(set2)  
print(set3)  

# Create three sets  
set1 = {1, 2, 3}  
set2 = {2, 3, 4}  
set3 = {3, 4, 5}  
# Find the common elements between the three sets  
common_elements = set1.intersection(set2, set3)  
# Print the common elements  
print(common_elements)