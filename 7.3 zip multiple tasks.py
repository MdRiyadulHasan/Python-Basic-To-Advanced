numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summation = [x+y for x,y in zip(numbers1,numbers2)]
print(summation)
print(sum(summation))

numbers = [1, 2, 3, 4]
squares = [x * x for x in numbers]
cubes = [x * x * x for x in numbers]
combined = zip(numbers, squares, cubes)

print(list(combined))

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 28]
sorted_names = [age for age, name in sorted(zip(ages, names))]

print(sorted_names)

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 28]
salaries = [50000, 60000, 55000]
for name, age, salary in zip(names, ages,salaries):
    print(f'{name } is {age } years old and get bdt {salary}')

keys = ['a', 'b', 'c']
values = [1, 2, 3]
merged_dict = dict(zip(keys, values))
print(merged_dict)
