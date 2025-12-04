n = int(input())
recipe_items = [input().strip() for _ in range(n)]

filtered_items = [item for item in recipe_items if "лук" not in item.lower()]

print(", ".join(filtered_items))
