import re

pattern = r"hello"
string = "hello world hello"
print("rs.match.......")
result = re.match(pattern, string)

print(result)  # Output: <re.Match object; span=(0, 5), match='hello'>

print("rs.search.......")
result = re.search(pattern, string) 

if result:
    print(result.group())  # Output: hello


print("re.findall()...... One or more digits.")
pattern = r"\d+"
string = "There are 3 cats, 4 dogs, and 5 birds"
result = re.findall(pattern, string)

print(result)  # Output: ['3', '4', '5']

print(" re.sub().......# One or more spaces")
pattern = r"\s+"
string = "Python   is    great"
new_string = re.sub(pattern, " ", string)

print(new_string)  # Output: Python is great

print("Email Validation")
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
email = "test.email@example.com"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")