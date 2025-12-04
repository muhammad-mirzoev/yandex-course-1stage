n = int(input())
sets = [list(map(int, input().split())) for _ in range(n)]

medians = []
modes = []
all_numbers = []

for s in sets:
    s_sorted = sorted(s)
    medians.append(s_sorted[len(s_sorted) // 2])
    mode = max(set(s), key=s.count)
    modes.append(mode)
    all_numbers.extend(s)

median_of_medians = sorted(medians)[len(medians) // 2]
mode_of_modes = max(set(modes), key=modes.count)

median_of_all = sorted(all_numbers)[len(all_numbers) // 2]
mode_of_all = max(set(all_numbers), key=all_numbers.count)

print(*medians)
print(*modes)
print(median_of_medians)
print(mode_of_modes)
print(median_of_all)
print(mode_of_all)
