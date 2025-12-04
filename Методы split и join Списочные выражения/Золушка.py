s = input()
words = input().split()
print(*[word for word in words if s in word])
