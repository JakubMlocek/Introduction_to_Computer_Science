def czypierwsza(liczba):
    if liczba < 2:
        return False
    i = 2
    while i*i <= liczba:
        if liczba % i == 0:
            return False
        i += 1
    return True

def bin2dec(bin):
    pot = 1
    wynik = 0
    i = len(bin) - 1
    while i >= 0:
        wynik = wynik + bin[i] * pot
        pot *= 2
        i -= 1
    return wynik

def pociecie(T):
    if czypierwsza(bin2dec(T)):
        return True
    else:
        for i in range(2,len(T)):
            if czypierwsza(bin2dec(T[:i])):
                return pociecie(T[i:])
        return False

t=[1,1,1,0,1,1]
print(pociecie(t))