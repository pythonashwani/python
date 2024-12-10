Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1|Days2) #printing the union of the sets     
print(Days1.union(Days2)) #printing the union of the sets

# Create three sets  
set1 = {1, 2, 3}  
set2 = {2, 3, 4}  
set3 = {3, 4, 5}
# Find the common elements between the three sets  
common_elements = set1.union(set2, set3)  
# Print the common elements  
print(common_elements)  
