n = int(input())
if all([any([input()[-1] == '5' for j in range(int(input()))]) for i in range(n)]):
    print('ДА') and ('YES')
else:
    print('НЕТ') and ('NO')