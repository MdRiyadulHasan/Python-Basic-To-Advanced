def sortedJson(peopleList):
    ans  = sorted(peopleList, key = lambda person: person['age'], reverse = True)
    return ans
if __name__ == "__main__":
    peoples = [
        {
            "name": "Alice",
            "email": "alice@gmail.com",
            "age": 25,
        },

        {
            "name": "Bob",
            "email": "bob@gmail.com",
            "age": 30
        },

        {
            "name": "Charlie", 
            "email": "charlie@gmail.com",
            "age": 22
        },
        {
            "name": "Milton", 
            "email": "milton@gmail.com",
            "age": 28
        }
    ]

    res = sortedJson(peoples)
    print(res)
