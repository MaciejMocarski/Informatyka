def func(x):
    return 2 * x - 2

a = -1
b = 4
e = 0.0001

if func(a) * func(b) <= 0:
    while abs(a - b) > e:
        s = (a + b) / 2
        if func(a) * func(s) <= 0:
            b = s
        else:
            a = s

print(s)