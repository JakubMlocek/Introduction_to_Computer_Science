def czy_wielokrotnosc_kwadratu_l_naturalnej(liczba):
    for l in range(2,liczba + 1):
        if liczba % (l * l) == 0 and (liczba // (l * l)) >= 2:
            return True
    return False

def sprpowybraniu(T, N, delwiersz, delkol1, delkol2):
    for wiersz in range(N):
        if wiersz == delwiersz:
            continue
        for kol in range(N):
            if kol == delkol1 or kol == delkol2:
                continue
            if not czy_wielokrotnosc_kwadratu_l_naturalnej(T[wiersz][kol]):
                return False
    return True

def czy_usuwanie(T, N):
    for delwiersz in range(N):
        for delkol1 in range(N):
            for delkol2 in range(N):
                if delkol1 == delkol2:
                    continue
                #print(f"{delwiersz} {delkol1} {delkol2} \n")
                if sprpowybraniu(T, N, delwiersz, delkol1, delkol2):
                    return True
    return False

T = [[16,16,16,16],
     [16,16,16,16],
     [16,16,16,16],
     [16,16,16,16]]

#print(czy_wielokrotnosc_kwadratu_l_naturalnej(16))
print(czy_usuwanie(T,4))