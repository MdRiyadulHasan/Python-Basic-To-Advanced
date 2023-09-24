data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
for i,n in enumerate(data['children']):
    print(data['children'][i]['firstName'], data['children'][i]['age'])
print("...........hlw data..................")
for i,n in enumerate(data['hobbies']):
    print(data['hobbies'][i])