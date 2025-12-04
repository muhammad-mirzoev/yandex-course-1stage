n = int(input())
m = int(input())
image = [input() for _ in range(n)]

for i in range(0, n, 2):
    compressed_row = image[i][0::2]
    print(compressed_row)
