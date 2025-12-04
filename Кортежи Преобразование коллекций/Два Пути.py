s = int(input())

brother1 = [int(input()) for _ in range(s)]
brother2 = brother1[:]

n = int(input())

for _ in range(n):
    brother = int(input())
    index = int(input())
    increase = int(input())
    if brother == 1:
        brother1[index] += increase
    else:
        brother2[index] += increase

print(" ".join(map(str, brother1)))
print(" ".join(map(str, brother2)))
matches = sum(1 for i in range(s) if brother1[i] == brother2[i])
print(matches)
