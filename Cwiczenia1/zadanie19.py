def silnia(liczba):
    if liczba == 0:
        return 1
    else:
        return liczba*silnia(liczba-1)

dokladnosc = 10

e = 0
for i in range(dokladnosc):
    e += 1/silnia(i)

print(e)
