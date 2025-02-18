def suma_liczb(n):
    return sum(int(i) for i in str(n))

with open("trojki.txt", "r") as plik:
    lines = plik.readlines()

wyniki = []

for line in lines:
    a, b, c = map(int, line.split())
    if suma_liczb(a) + suma_liczb(b) == c:
        wyniki.append(f"{a} {b} {c}")

# Zapisanie wyników do pliku wyjściowego
with open("wyniki_trojki.txt", "w") as output_file:
    output_file.write("\n".join(wyniki))

print("Zapisano w trojki_wyniki.txt")
