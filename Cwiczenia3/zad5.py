dziesiecnajw = [0 for _ in range(10)]
liczba = int(input("Podaj Liczbe:  "))
while liczba != 0:
    dziesiecnajw.append(liczba)
    dziesiecnajw = sorted(dziesiecnajw, reverse = True)
    dziesiecnajw = dziesiecnajw[:10]
    print(dziesiecnajw)
    liczba = int(input("Podaj Liczbe:  "))

print(dziesiecnajw[9])