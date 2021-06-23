def iloczynominroznicy(liczba):
    minodl = liczba
    dzielnik = liczba
    for i in range(1, liczba + 1):
        if liczba % i == 0:
            if abs(i - liczba // i) < minodl:
                minodl = abs(i - liczba // i)
                dzielnik = i
    return dzielnik, liczba // dzielnik

liczba = int(input("liczba:  "))
print(iloczynominroznicy(liczba))


