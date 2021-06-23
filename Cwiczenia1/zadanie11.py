def sumapodzielnikow( liczba ):
    podzielnik = 1
    suma = 0
    while podzielnik < liczba:
        if liczba % podzielnik == 0:
            suma += podzielnik
        podzielnik += 1
    return suma


for i in range(10**6):
    nowa = sumapodzielnikow(i)
    if i > nowa:
        if sumapodzielnikow(nowa) == i:
            print(str(i) + "\n" + str(nowa))