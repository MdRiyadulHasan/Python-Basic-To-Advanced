def findBestScore1(scores):
    ans = sorted(scores.items(), key = lambda val : val[0], reverse = True)
    return ans
def findBestScore(nums):
    ans = sorted(nums.items(), key = lambda x : x[1], reverse = True)
    return ans
if __name__ == "__main__":
    scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
    res = findBestScore(scores)
    res1 = findBestScore1(scores)
    print(res)
    print(res1)
