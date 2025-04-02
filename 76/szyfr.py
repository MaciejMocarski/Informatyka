def szyfruj_napis(napis, klucz):
    n = len(klucz)
    napis = list(napis)
    for i in range(len(napis)):
        pozycja = klucz[i % n] - 1
        napis[pozycja] = napis[i]
        napis[i] = napis[pozycja]
    return ''.join(napis)

with open('python/76/szyfr1.txt', 'r') as plik:
    linie = plik.readlines()
    
napisy = [linie[i].strip() for i in range(6)]
klucz = list(map(int, linie[6].strip().split()))

zaszyfrowane_napisy = [szyfruj_napis(napis, klucz) for napis in napisy]

print(zaszyfrowane_napisy)