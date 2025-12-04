n = int(input())

for _ in range(n):
    advice = input().strip()

    if advice[:3].lower() == "не ":
        advice = advice[3:]

    print(advice)
