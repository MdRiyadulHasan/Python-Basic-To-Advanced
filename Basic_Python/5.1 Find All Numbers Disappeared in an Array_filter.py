def missingNums(nums):
    allNums = list(set(range(1, len(nums)+1)))
    existingNums = list(set(nums))
    print(existingNums)
    print(allNums)
    ans = list(filter(lambda x: x not in existingNums, allNums))
    return ans

def findDisappearedNumbers(nums):
    allNums = list(set(range(1,len(nums)+1)))
    existingNums = list(set(nums))
    ans = list(filter(lambda x: x not in existingNums, allNums ))
    return ans

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    ans = missingNums(nums)
    ans2 = findDisappearedNumbers(nums)
    print(ans)
    print(ans2)