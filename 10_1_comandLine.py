# python ./10_1_comandLine.py  1 add 3
# python ./10_1_comandLine.py  9 sub 3
# python ./10_1_comandLine.py  6 mult 3
# alias calc="python3 ./10_1_comandLine.py"
# calc 1 add 3
# calc 9 sub 3
# calc 6 mult 3
import sys

num1 = int(sys.argv[1])
operator = sys.argv[2]
num2 = int(sys.argv[3])

if operator == 'add':
    output = num1 + num2
    print (output)
elif operator == 'sub':
    output = num1 - num2
    print (output)
elif operator == 'mult':
    output = num1 * num2
    print(output)
else: 
    print("Please give the correct operator, Any one( add, sub, multi)")