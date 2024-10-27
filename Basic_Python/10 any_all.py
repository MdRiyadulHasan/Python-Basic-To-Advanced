nums = [1, 2, 3, 4, 5]
hasEven = any(num%2==0 for num in nums)
allPositive = all(n>=0 for n in nums)
print(hasEven)
print(allPositive)


