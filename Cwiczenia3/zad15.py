def elementyfib(zakres):
    elementy = []
    a = 1
    b = 1
    while a < zakres:
        a, b = b, a + b
        elementy.append(a)
    return elementy

def czypierwsza(liczba):
    if liczba < 2:
        return False
    i = 2
    while i * i <= liczba:
        if liczba % i == 0:
            return False
        i += 1
    return True

def czywarunki(tab):
    bool czywpozostalychpierwsza = False
    elfib = elementyfib(len(tab))
    for indeks in range(tab):
        if indeks in elfib:
            if not czypierwsza(tab[indeks]):
                return False
        else:
            if czypierwsza(tab[indeks]):
                czywpozostalychpierwsza = True
    return czywpozostalychpierwsza

