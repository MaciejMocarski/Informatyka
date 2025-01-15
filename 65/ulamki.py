import os

liczniki = []
mianowniki = []
file_path = os.path.join(os.path.dirname(__file__), 'dane_ulamki.txt')

with open(file_path, 'r') as file:
    for linia in file.readlines():
        liczby = linia.split()
        liczniki.append(int(liczby[0]))
        mianowniki.append(int(liczby[1]))
# print(liczniki)
# print(mianowniki)
min_ulamek = [liczniki[0], mianowniki[0]]
ulamek = []
for i in range(1, len(liczniki)):
    liczba = liczniki[i] / mianowniki[i]
    if liczba < min_ulamek[0] / min_ulamek[1]:
        if liczba == min_ulamek[0] / min_ulamek[1]:
            if min_ulamek[0] > liczniki[i]:
                min_ulamek[0] = liczniki[i]
                min_ulamek[1] = mianowniki[0]
        else:
            min_ulamek[0] = liczniki[i]
            min_ulamek[1] = mianowniki[i]
print(min_ulamek)