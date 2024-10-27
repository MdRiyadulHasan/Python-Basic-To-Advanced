words = ["apple", "banana", "cherry", "date", "grape", "kiwi"]

ans = list(filter(lambda x: len(x)>=5, words))

print(ans)