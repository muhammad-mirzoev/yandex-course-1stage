s = input().strip()

for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        print(s[i + 1])
        break
else:
    print("(:_0_:)")
