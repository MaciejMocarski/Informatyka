P = float(input())
a = 1
b = P

e = 0.00000000000000000000000001

while abs(a - b) > e:
    a = (a + b) / 2
    b = P / a

print(b)