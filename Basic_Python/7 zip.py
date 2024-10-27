names = ['Alice', 'Bob', 'Charlie', 'Adam', 'Milton']
ages = [25, 30, 28, 22, 26]

combined = list(zip(names,ages))

sortingUsingAge = sorted(combined, key = lambda x:-x[1])

sortedUsingName = sorted(combined, key = lambda x:x[0], reverse = True)

print(combined)

print(sortingUsingAge)

print(sortedUsingName)