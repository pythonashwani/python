# Arithmetic Operators
'''
x = 2
y = 7

total = x + y
print(total)

total = x - y
print(total)

total = x * y
print(total)

total = y/x
print(total)

total = y % x
print(total)

total = y**x
print(total)

# Comparison Operators

a = 30
b = 60

out = (a < b)
print(out)


out = (a > b)
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a >= b)
print(out)

out = (a <= b)
print(out)

# Assignment Operators

c = 0
d = 1

#c+=d # c = c+d

print(c)

c-=d # c = c-d
print(c)

# Logical Operators

# and - must be true
# or - any one true
'''
a = 40
b = 60

x = 2
y = 3
print('* ' * 10)
out = (a < b) or (x > y)
print(out) # True

out = (a > b) or (x < y)
print(out) # True

out = (a > b) or (x > y)
print(out) 

out = (a > b) and (x < y)
print(out)

out = (a < b) and (x < y)
print(out)

out = not(x < y)
print(out)

# Membership Operator

first_tuple = ("IOT", "DevOps", 47, 89, 1.5)
ans = "DevOps" in first_tuple
print(ans)

ans = "DevOps" not in first_tuple
print(ans)

ans = 67 not in first_tuple
print(ans)

# Identity Operators
a = 12
b = 15

result = a is b
print(result)

result = a is not b
print(result)

print('#'  * 10)

a = 100
p = a << 2
print(p)
p = a >> 2
print(p)
'''

256	128	64	32	16	8	4	2	1			
0	0	1	1	0	0	1	0	0		100	
1	1	0	0	1	0	0	0	0		100<<2	400(=256+128+16)
0	0	0	0	1	1	0	0	1		100>>2	25 (=16+8+1)



z = 10 + 2 * 3 - 4 / 2 + 1
print(z)
'''

