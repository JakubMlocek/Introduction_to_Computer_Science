liczba = 2315
cyfry = len(str(liczba))

ilosc = 0

for maska in range (1, 2**cyfry):
    sprawdzana = 0
    liczba1 = liczba
    pow10 = 1

    while maska > 0:
        #1 - cyfra zostaje
        #0 - cyfra usuwana
        if maska % 2 == 1:
            cyfra = liczba1 % 10
            sprawdzana += cyfra * pow10
            pow10 *= 10
        maska //= 2
        liczba1 //= 10

    if sprawdzana % 7 == 0:
        ilosc += 1

print(ilosc)