def UpperToLower(name):
    return name.lower()

def transformLower(names):
    names1 = list(map(UpperToLower, names))
    return names1

def transformLower2(names):
    names2 = list(map(lambda x : x.lower(), names))
    return names2

# Complete Example 
def findResult(names):
    names = [i.lower() for i in names]
    res = list(filter(lambda x: x.startswith('a'), names))
    return res

if __name__ == '__main__':
    nameList = ["Alice", "Bob", "Charlie", "David", "Eva", "Arif", "Saad", "Arman"]
    ans = findResult(nameList)
    ans1 = transformLower(nameList)
    ans2 = transformLower2(nameList)
    print(ans)
    print(ans1)
    print(ans2)