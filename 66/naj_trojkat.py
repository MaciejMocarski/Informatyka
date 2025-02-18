def trojkatChecker(a, b, c):
    bok = sorted([a, b, c])
    return bok[0] + bok[1] > bok[2]

with open("trojki.txt", "r") as plik:
    linia = [list(map(int, line.split())) for line in plik]

ilosc_trojkatow = 0
najdluzszy_ciag = 0
ciag = 0

for line in linia:
    if trojkatChecker(*line):
        ilosc_trojkatow += 1
        ciag += 1
        najdluzszy_ciag = max(najdluzszy_ciag, ciag)
    else:
        ciag = 0

print(f"Liczba wierszy reprezentujących trójkąty: {ilosc_trojkatow}")
print(f"Najdłuższy ciąg wierszy trójkątów: {najdluzszy_ciag}")