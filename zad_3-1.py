file = open("pi.txt")
wiersze = file.readlines()

wynik = 0

for i in range(0, len(wiersze), 1):
    if i != len(wiersze) - 1:
        if int(wiersze[i].strip() + wiersze[i + 1].strip()) > 90:
            wynik += 1

print(wynik)
assert wynik == 902
