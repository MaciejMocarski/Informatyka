def decToAll(liczba, sys):
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % sys) + wynik
        liczba = liczba // sys
    return wynik

print(decToAll(45, 8))