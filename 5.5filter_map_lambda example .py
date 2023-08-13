numbers = [1, 2, 3, 4, 5,2,-1,10,12,-15,8]
squared_numbers = list(map(lambda x : x**2, numbers))
even_numbers = list(filter(lambda x: x%2==0, numbers))
sorted_numbers = sorted(numbers, key = lambda x: x)

print(squared_numbers)
print(even_numbers)     
print(sorted_numbers)         
