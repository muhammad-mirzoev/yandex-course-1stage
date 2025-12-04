M = int(input())
fridge = set(input().strip() for _ in range(M))

N = int(input())
recipes = []

for _ in range(N):
    recipe_name = input().strip()
    K = int(input())
    ingredients = set(input().strip() for _ in range(K))

    if ingredients.issubset(fridge):
        recipes.append(recipe_name)

for recipe in recipes:
    print(recipe)
