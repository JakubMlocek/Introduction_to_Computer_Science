def dec2any(liczba, system):
    wynik = ""
    while(liczba >= 1):
        if liczba % system < 10:
            wynik = str(liczba % system) + wynik
        else:
            #print(liczba % system)
            wynik = chr(liczba % system + 55) + wynik
        liczba //= system
    return wynik

def dec2anyv2(liczba, system):
    zmienione = []
    cyfry = "0123456789ABCDEF"
    while liczba > 0:
        reszta = liczba % system
        liczba //= system
        zmienione.append(cyfry[reszta])
    zmienione.reverse()
    return zmienione


print(dec2any(2347895,8))
print(dec2anyv2(2347895,8))


