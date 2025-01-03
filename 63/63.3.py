import os

ciagi = []
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "ciagi.txt")

with open(file_path, "r") as f:
    for linia in f:
        ciagi.append(linia.strip())

liczbyDz = []
def horner(liczba, x):
    wynik = int(liczba[0])
    for i in range(len(liczba)):
        wynik = wynik * x + int(liczba[i])
    return wynik

for i in range(len(ciagi)):
    liczbyDz.append(horner(ciagi[i], 2))
# print(liczbyDz)
liczbyPierw = []
liczby = []
for i in range(270000):
    liczby.append(1)
for i in range(2, 270000):
    if liczby[i] == 1:
        for j in range(i+i, 270000, i):
            liczby[j] = 0
for i in range(2, 270000):
    if liczby[i] == 1:
        liczbyPierw.append(i)
# print(liczbyPierw)

for i in range(len(liczbyDz)):
    czynniki = []
    liczba = liczbyDz[i]
    for j in range(len(liczbyPierw)):
        while (liczba % liczbyPierw[j] == 0):
            liczba = liczba // liczbyPierw[j]
            czynniki.append(liczbyPierw[j])
        if len(czynniki) > 2:
            break
    else:
        if len(czynniki) == 2:
            print(liczbyDz[i], czynniki)
            