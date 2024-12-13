def f(x):
    return x**2

def pole_pod_wykresem(a, b, E):
    n = E
    dx = (b - a) / n
    pole = 0

    for i in range(n):
        x = a + i * dx
        pole += f(x) * dx

    return pole

a = 0
b = 1
E = 1000
wynik = pole_pod_wykresem(a, b, E)
print(f"Pole powierzchni pod wykresem funkcji w przedziale <{a},{b}> wynosi: {wynik:.5f}")