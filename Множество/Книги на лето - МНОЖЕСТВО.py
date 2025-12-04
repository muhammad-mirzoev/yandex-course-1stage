M = int(input())
N = int(input())

library = set()

for _ in range(M):
    book = input().strip()
    library.add(book)

for _ in range(N):
    book = input().strip()
    if book in library:
        print("YES")
    else:
        print("NO")
