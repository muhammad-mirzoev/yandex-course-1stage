text = input().strip().lower()
frequency = {}

for char in text:
    if char not in frequency:
        frequency[char] = 1
    else:
        frequency[char] += 1

max_count = max(frequency.values())

print(max_count)
