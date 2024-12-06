# w0 = 1
# w1 = w0*2+1
# w2 = w1*2+0
# w3 = w2*2+1
# w4 = w3*2+0 = 26

def horner(liczba, x):
    wynik = int(liczba[0])
    for i in range(len(liczba)):
        wynik = wynik * x + int(liczba[i])
    return wynik

print(horner('110101', 2))