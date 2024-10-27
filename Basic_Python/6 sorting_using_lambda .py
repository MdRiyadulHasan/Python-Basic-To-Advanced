def sortWords(wordList):
    return sorted(wordList, key = lambda x : -len(x))
if __name__ == '__main__':
    words = ['apples', 'banana', 'cherry', 'date','Bangladesh', 'Pakistan','Bat']
    ans = sortWords(words)
    print(ans)