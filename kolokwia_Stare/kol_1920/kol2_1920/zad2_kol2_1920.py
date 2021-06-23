def zwieksz_parzyste_cyfry(liczba):
    po_zwiekszeniu = 0
    mnoznik = 1
    while liczba > 0:
        cyfra = liczba % 10
        if cyfra % 2 == 0:
            cyfra += 1
        po_zwiekszeniu += cyfra * mnoznik
        liczba //= 10
        mnoznik *= 10
    return po_zwiekszeniu

wszystkie_mozliwosci = []
def przeksztalc(liczba, oczekiwana, liczbakrokow, ostatnia_operacja = "D",uzyte_operacje = []):
    global wszystkie_mozliwosci
    if liczba == oczekiwana:
        wszystkie_mozliwosci.append(uzyte_operacje)
    if liczbakrokow > 0:
        if ostatnia_operacja != "A":
            przeksztalc(liczba + 3, oczekiwana, liczbakrokow - 1,"A", uzyte_operacje + ["A"])
        if ostatnia_operacja != "B":
            przeksztalc(liczba * 2, oczekiwana, liczbakrokow - 1, "B",uzyte_operacje + ["B"])
        if ostatnia_operacja != "C":
            przeksztalc(zwieksz_parzyste_cyfry(liczba), oczekiwana, liczbakrokow - 1, "C", uzyte_operacje + ["C"])
przeksztalc(11,31,4)
print(wszystkie_mozliwosci)
print(len(wszystkie_mozliwosci))