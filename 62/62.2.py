def read_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def horner(i, x):
    dziesietny = int(i[0])
    for digit in i[1:]:
        dziesietny = dziesietny * x + int(digit)
    return dziesietny

def decToAll(i, sys):
    wynik = ""
    while i > 0:
        remainder = i % sys
        if remainder >= 10:
            wynik = chr(55 + remainder) + wynik
        else:
            wynik = str(remainder) + wynik
        i //= sys
    return wynik

def longestStreak(lista):
    najdluzszy_ciag = 0
    aktualny_ciag = 1
    pierwszy_element = lista[0]
    aktualny_pierwszy = lista[0]

    for i in range(1, len(lista)):
        if lista[i] >= lista[i - 1]:
            aktualny_ciag += 1
        else:
            if aktualny_ciag > najdluzszy_ciag:
                najdluzszy_ciag = aktualny_ciag
                pierwszy_element = aktualny_pierwszy
            aktualny_ciag = 1
            aktualny_pierwszy = lista[i]
    if aktualny_ciag > najdluzszy_ciag:
        najdluzszy_ciag = aktualny_ciag
        pierwszy_element = aktualny_pierwszy

    return pierwszy_element, najdluzszy_ciag


lista = read_file("liczby2.txt")
pierwszy_element, najdluzszy_ciag = longestStreak(lista)
print(f"Pierwszy element: {pierwszy_element}, długość: {najdluzszy_ciag}")
