file = open("bin.txt")
wiersze = file.readlines()

max = 0
wynik = ""

for wiersz in wiersze:
    wiersz = wiersz.strip()
    dziesietna = int(wiersz, 2)
    if dziesietna > max:
        max = dziesietna
        wynik = wiersz

assert wynik == "1110100011100011100"
