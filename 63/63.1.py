import os

ciagi = []
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "ciagi.txt")

with open(file_path, "r") as f:
    for linia in f:
        ciagi.append(linia.strip())
# print(ciagi)
for i in range(len(ciagi)):
    if ciagi[i][0:len(ciagi[i])//2] == ciagi[i][len(ciagi[i])//2:]:
        print(ciagi[i])