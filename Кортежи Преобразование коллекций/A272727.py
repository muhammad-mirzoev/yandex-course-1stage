n = int(input())

sequence = [0]

for i in range(1, n):
    count_matches = sum(1 for j in range(i) if sequence[j] == sequence[i - j - 1])
    sequence.append(count_matches)

print("\n".join(map(str, sequence)))
