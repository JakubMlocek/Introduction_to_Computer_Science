import random
def czynniki(liczba):
    tabczynnikow = []
    dzielnik = 2
    while liczba > 1:
        if liczba % dzielnik == 0:
            tabczynnikow.append(dzielnik)
            while(liczba % dzielnik == 0):
                liczba //= dzielnik
        else:
            dzielnik += 1
    return tabczynnikow

tab = [2,3,5,6,1,10,14,15]
czymoznazpierwszego = [False]*len(tab)
czymoznazpierwszego[0] = True
for i in range(len(tab)):
    if czymoznazpierwszego[i] == True:
        for czynnik in czynniki(tab[i]):
            if czynnik <= len(tab) - i - 1: #czy nie wyjdziemy poza tablice
                czymoznazpierwszego[i + czynnik] = True

print(czymoznazpierwszego[len(tab) - 1])


