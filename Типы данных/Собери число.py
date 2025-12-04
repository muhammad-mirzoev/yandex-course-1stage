number = int(input().strip())

a = number // 100
b = (number // 10) % 10
c = number % 10

sum1 = a + b
sum2 = b + c

if sum1 > sum2:
    result = str(sum1) + str(sum2)
else:
    result = str(sum2) + str(sum1)

print(result)
