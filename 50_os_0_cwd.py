import os
print(os.getcwd()) # current working directory
os.chdir("..") # change directory
print(os.getcwd()) # current working directory
print(os.listdir()) # list the directory 
os.mkdir("Fruit") # creates a directory called Fruit
print(os.listdir())

print("Before Creating:", os.listdir())
os.makedirs("vehicles/four_wheeler/car")
print("After Creating:", os.listdir())
print("Directory created: vehicles/four_wheeler/car")


print("Before Removing:", os.listdir())
os.removedirs("vehicles/four_wheeler/car")
print("After Removing:", os.listdir())
print("Directory Removed: vehicles/four_wheeler/car")

print("Before Removing:", os.listdir())
os.rmdir("Fruit2")
print("After Removing:", os.listdir())
print("Directory Removed: Fruitr")

print("Before renaming:", os.listdir())
os.renames("apple.txt", "Mango.txt")
print("After renaming:", os.listdir())

print("Before removing:", os.listdir())
os.remove('Mango.txt')
print("After removing:", os.listdir())


for i, j, k in os.walk(os.getcwd()):
    print("path =", i)
    print("List of directories =", j)
    print("List of files =", k)

os.system("Python --version")
os.system("ls -ltra")
