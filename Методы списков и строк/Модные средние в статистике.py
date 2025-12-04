numbers = list(map(int, input().split()))

numbers.sort()
median = numbers[len(numbers) // 2]

total = {}
for num in numbers:
    if num in total:
        total[num] += 1
    else:
        total[num] = 1

mode = max(total, key=total.get)

print(median, mode)
