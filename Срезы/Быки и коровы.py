s1 = input().strip()
s2 = input().strip()

bulls = 0
cows = 0

remaining_s2 = list(s2)

for i in range(len(s1)):
    if s1[i] == s2[i]:
        bulls += 1
        remaining_s2[i] = None

for i in range(len(s1)):
    if s1[i] != s2[i]:
        if s1[i] in remaining_s2:
            cows += 1
            remaining_s2[remaining_s2.index(s1[i])] = None

print(bulls, cows)
