def sortedSquares(nums):
    return list(sorted (map(lambda x: x**2, nums)))

def sortedSquares2(nums):
    return sorted([x**2 for x in nums])

if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    result = sortedSquares(nums)
    result2 = sortedSquares2(nums)
    print(result)
    print(result2)