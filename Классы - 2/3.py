class X:
    def __call__(self, x):
        return x


class SQRT:
    def __call__(self, x):
        return x ** 0.5


d = {'x': X(), 'sqrt_fun': SQRT()}


class A:
    def __init__(self, znak, arg1, arg2):
        self.znak = znak
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, arg):
        if self.arg1 in d:
            a = d[self.arg1](arg)
        else:
            a = int(self.arg1)
        b = d[self.arg2](arg)
        if self.znak == '+':
            return a + b
        if self.znak == '-':
            return a - b
        if self.znak == '*':
            return a * b
        if self.znak == '/':
            return a / b
        if self.znak == '//':
            return a // b


n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == 'define':
        d[s[1]] = A(s[3], s[2], s[4])
    if s[0] == 'calculate':
        g = s[2:]
        g = [int(j) for j in g]
        ans = d[s[1]]
        for u in g:
            print(ans(u), end=' ')