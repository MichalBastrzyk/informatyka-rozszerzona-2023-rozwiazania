file = open("bin.txt")
wiersze = file.readlines()

wynik = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()

    prev = wiersz[0]
    ilosc_blokow = 1
    for char in wiersz:
        if prev != char:
            ilosc_blokow += 1
            prev = char

    if ilosc_blokow <= 2:
        wynik += 1

print(wynik)
