def zwroc_czynniki(liczba):
    tab_czynniki = []
    czynnik = 2
    while liczba > 1:
        if liczba % czynnik == 0:
            tab_czynniki.append(czynnik)
        while liczba % czynnik == 0:
            liczba //= czynnik
        czynnik += 1
    return tab_czynniki


ileskokow = 0
def skok(T, pozycja = 0, ilosc_skokow = 0):
    if pozycja == len(T) - 1:
        global ileskokow
        ileskokow = ilosc_skokow
    liczba = T[pozycja]
    czynniki = zwroc_czynniki(liczba)
    for czynnik in czynniki:
        if pozycja + czynnik < len(T):
            skok(T, pozycja + czynnik, ilosc_skokow + 1)

def skokv2(T, pozycja = 0, ilosc_skokow = 0):
    if pozycja == len(T) - 1:
        return ilosc_skokow
    liczba = T[pozycja]
    czynniki = zwroc_czynniki(liczba)
    for czynnik in czynniki:
        if pozycja + czynnik < len(T):
            ilosc = skokv2(T, pozycja + czynnik, ilosc_skokow + 1)
            if ilosc != -1:
                return ilosc
    return -1

T = [6,1,1,6,1,1,6,1,1]
print(skokv2(T))
