lista = []
with open("liczby2.txt", "r") as plik:
    for i in plik.readlines():
        lista.append(int(i.strip()))

wystepujace10 = 0
wystepujace8 = 0

for i in lista:
    licznik = 0
    for j in str(i):
        if j == '6':
            licznik += 1
    wystepujace10 += licznik

    liczba_8 = ""
    temp = i
    while temp > 0:
        liczba_8 = str(temp % 8) + liczba_8
        temp //= 8

    licznik_osemkowy = 0
    for j in liczba_8:
        if j == '6':
            licznik_osemkowy += 1
    wystepujace8 += licznik_osemkowy
print(f"10: {wystepujace10}, 8: {wystepujace8}")

