n = int(input())
items = [input().strip() for _ in range(n)]

k = int(input())

current_items = items
for _ in range(k):
    ni = len(current_items)
    ni1 = int(input())
    new_order = [int(input()) - 1 for _ in range(ni1)]

    current_items = [current_items[i] for i in new_order]

print("\n".join(current_items))
