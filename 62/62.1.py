lista = []
with open("liczby1.txt", "r") as plik1:
    for i in plik1.readlines():
        lista.append(i.strip())

def horner(i, x):
    dziesietny = int(i[0])
    for i in range(1, len(i)):
        dziesietny = dziesietny * x + int(i[i])
    return dziesietny

def decToAll(i, sys):
    wynik = ""
    while i > 0:
        remainder = i % sys
        if remainder >= 10:
            wynik = chr(55 + remainder) + wynik
        else:
            wynik = str(remainder) + wynik
        i = i // sys
    return wynik

maks1 = -1
min1 = float('inf')
num_max = ""
num_min = ""

for i in lista:
    i_dziesietna = horner(i, 8)
    if i_dziesietna > maks1:
        maks1 = i_dziesietna
        num_max = i
    if i_dziesietna < min1:
        min1 = i_dziesietna
        num_min = i

maks1 = decToAll(maks1, 8)
min1 = decToAll(min1, 8)
print(f"Max: {num_max} -> {maks1}, Min: {num_min} -> {min1}")
