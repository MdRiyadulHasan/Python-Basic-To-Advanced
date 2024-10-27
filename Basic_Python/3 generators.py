def squareNumbers(nums):
    for n in nums:
        if n%2 == 0:
            yield n**2 
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5,6,7,8]
    ans = squareNumbers(nums)
    print(list(ans))