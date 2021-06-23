#Jakub Młocek

from math import log10
from math import floor

def czypierwsza(liczba):
    if liczba < 2:
        return False
    i = 2
    while i * i <= liczba:
        if liczba % i == 0:
            return False
        i += 1
    return True

def Tnij(n,podzial = []):
    #jezeli liczba kawalkow + 1 jest pierwsza i ostatni kawalek jest liczba pierwsza to zwracamy prawde
    if czypierwsza(len(podzial) + 1) and czypierwsza(n):
        return True
    dl = floor(log10(n)) + 1  # dlugosc liczby
    for i in range(1,dl):
        #idziemy po dlugosci liczby i dzielimy na dwa fragmenty
        zostaje = n % (10 ** i)
        zabrane = n//(10**i)
        #dodajemy tylko gdy fragment jest liczba pierwsza
        if czypierwsza(zabrane):
            return Tnij(zostaje, podzial+[n//(10**i)])
    return False

#aby nie dodawac własne argumentu domyslnego musiałem to zrobic w osobnej funkcji
def divide(n):
    return Tnij(n)

