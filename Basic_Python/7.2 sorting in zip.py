names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 28]

sorted_data = sorted(zip(names, ages), key=lambda x: x[1])

sorted_names, sorted_ages = zip(*sorted_data)

print(sorted_names)  
print(sorted_ages)  
