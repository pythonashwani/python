import json
# Script to parse JSON
json = json.loads(open('python.json').read())
value = json['Name']
print(value)

# Loop through JSON

for key in json:
    value = json[key]
    print("The key and value are ({}) = ({})".format(key, value))