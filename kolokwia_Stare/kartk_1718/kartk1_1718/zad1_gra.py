def dec2any(liczba, system):
    wynik = ""
    while(liczba > 0):
        dodaj = liczba % system
        if dodaj < 10:
            wynik = str(dodaj) + wynik
        else:
            wynik = chr(dodaj + 55) + wynik
        liczba //= system
    return wynik

def czyroznocyfrowe(liczba1, liczba2):
    for cyfra in liczba1:
        if cyfra in liczba2:
            return False
    return True

def app():
    liczba1 = 123
    liczba2 = 522
    for podstawa in range(2,16+1):
        if czyroznocyfrowe(dec2any(liczba1,podstawa),dec2any(liczba2,podstawa)):
            return podstawa
    return "NI MO"

print(app())