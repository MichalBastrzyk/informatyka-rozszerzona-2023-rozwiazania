file = open("pi.txt")
wiersze = file.readlines()

wynik = 0
dict = {}

# Fill the dict with keys
for i in range(0, 99, 1):
    dict[str(i).zfill(2)] = 0

for i in range(0, len(wiersze), 1):
    if i != len(wiersze) - 1:
        x = wiersze[i].strip() + wiersze[i + 1].strip()
        if x in dict:
            dict[x] += 1


print(f"{min(dict, key=dict.get)} {min(dict.values())}")
print(f"{max(dict, key=dict.get)} {max(dict.values())}")
