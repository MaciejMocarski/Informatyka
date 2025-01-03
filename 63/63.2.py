import os

ciagi = []
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "ciagi.txt")

with open(file_path, "r") as f:
    for linia in f:
        ciagi.append(linia.strip())

licznik = 0
for i in range(len(ciagi)):
    if not "11" in ciagi[i]:
        licznik += 1
print(licznik)