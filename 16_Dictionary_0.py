employee = {"name": "Johnny", "age": 32, "salary":26000,"company":"Devops"}
print(type(employee))
print("printing Employee data .... ")
print(employee)
print(type(employee))
print("Iterate all keys")
for x in employee:
    print(x)
print("Iterate all values")
for x in employee.values():
    print(x)
print("Iterate all keys=values")
for x,y in employee.items():
    print(x,y)

print(employee["name"])
print(employee.get("name"))

print("Update the properties")
employee["name"] = "Developer"
employee.update({"name": "Operation"})
employee["address"]= "NOIDA" # create the new key=value if not exists

print("printing the modified information ")
print(employee)



print("delete the employee company")
#del employee["company"] # delete the employee company
employee.pop("company")
print("printing the modified information ")
print(employee)
del employee
print("Lets try to print it again ");
#print(employee)