# map(function, iterable)
def squareValues(x):
    return x**2
nums = [2,4,6,7,8,-11,12,-13]
results = map(squareValues, nums)
print(list(results))

# using lambda function

results1 = list(map(lambda x: x**2, nums ))
print(results1)
