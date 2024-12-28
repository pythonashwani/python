# python3 ./10_0_comandLine.py  1 2 3
import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Print all command line arguments
print("Arguments Passed:", sys.argv) # ['10_0_comandLine.py', '1', '2', '3']

# Print the Script Name
print("Script Name:", sys.argv[0]) # 10_0_comandLine.py

# Print First Argument
print("First Argument:", sys.argv[1]) # 1

# Print Second Argument
print("Second Argument:", sys.argv[2]) # 2

# Print Third Argument
print("Third Argument:", sys.argv[3]) # 3