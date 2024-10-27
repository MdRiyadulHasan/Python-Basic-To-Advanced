numbers = [1, 2, 3, 4, 5,-7,-9,10,12]
squared_numbers = [x**2 for x in numbers]
even_squared_numbers = [x**2 for x in numbers if x%2==0]

print(squared_numbers)
print(even_squared_numbers)