n = int(input())

for _ in range(n):
    cubes = list(map(int, input().split()))

    left, right = 0, len(cubes) - 1
    last = float('inf')

    result = []

    while left <= right:
        if cubes[left] >= cubes[right] and cubes[left] <= last:
            result.append(cubes[left])
            last = cubes[left]
            left += 1
        elif cubes[right] <= last:
            result.append(cubes[right])
            last = cubes[right]
            right -= 1
        else:
            result = ["НЕТ"]
            break

    print(" ".join(map(str, result)))
