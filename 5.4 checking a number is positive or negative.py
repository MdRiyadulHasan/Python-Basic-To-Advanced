def findPositive(nums):
    res = list(filter(lambda x: x>0, nums))
    return res
def checkPositive(n):
    return n>0

def findPositive1(nums):
    res = list(filter(checkPositive, nums))
    return res

if __name__ == "__main__":
    numbers = [-2, -1, 0, 1, 2, -4,50,100,-5]
    ans = findPositive(numbers)
    ans1 = findPositive1(numbers)
    print(ans)
    print(ans1)