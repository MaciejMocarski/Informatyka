def kwadratowyChecker(a, b, c):
    bok = sorted([a, b, c])
    return bok[0]**2 + bok[1]**2 == bok[2]**2

with open("trojki.txt", "r") as plik:
    linia = [list(map(int, line.split())) for line in plik]

for i in range(len(linia) - 1):
    if kwadratowyChecker(*linia[i]) and kwadratowyChecker(*linia[i + 1]):
        print(f"{linia[i]}\n{linia[i + 1]}\n")
