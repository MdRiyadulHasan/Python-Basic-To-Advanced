names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 28]

combined = list(zip(names, ages))
print(combined)

unzipNames, unzipAge = zip(*combined)

print(list(unzipNames))

print(unzipAge)
