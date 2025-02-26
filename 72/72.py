lista_napisow = []
with open("72/napisy.txt") as plik:
    for linia in plik:
        lista_napisow.append(linia.split())

# 1.
# licznik = 0
# for napis in lista_napisow:
#     if len(napis[0]) >=  3*len(napis[1]) or len(napis[1]) >= 3*len(napis[0]):
#         if licznik < 1:
#             print("Zadanie 1:")
#             print(napis)
#         licznik += 1
# print(licznik)

# 2.
# for napis in lista_napisow:
#     if napis[0] == napis[1][:len(napis[0])]:
#         print(napis)

# 3.
def ileZnakowKoniec(napis1, napis2):
    n = 0
    if len(napis1) > len(napis2):
        for i in range(len(napis2)):
            if napis1[-1-i] != napis2[-1-i]:
                return n
            else:
                n += 1
        return n
    else:
        for i in range(len(napis2)):
            if napis1[-1-i] != napis2[-1-i]:
                return n
            else:
                n += 1
        return n

maks = 0
lista = []
for napis in lista_napisow:
    k = ileZnakowKoniec(napis[0], napis[1])
    if k > maks:
        maks = k
        lista = []
        lista.append(napis)
    elif k == maks:
        lista.append(napis)
print(maks, lista)