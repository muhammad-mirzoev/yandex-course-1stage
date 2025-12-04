text = input().strip()
count = 0

for char in text:
    if char not in [' ', '\t']:
        count += 1

print(count)
