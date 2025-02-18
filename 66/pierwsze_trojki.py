def pierwszaChecker(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

with open("trojki.txt", "r") as plik:
    lines = plik.readlines()

for line in lines:
    a, b, c = map(int, line.split())
    if pierwszaChecker(a) and pierwszaChecker(b) and c == a * b:
        print(f"{a} {b} {c}")