def czy_nieparzysta_l_jed_w_syst_2(liczba):
    ilejedynek = 0
    while liczba > 0:
        #print(f"{liczba}  {liczba % 2}")
        if liczba % 2 == 1:
            ilejedynek += 1
        liczba //= 2
    #print(ilejedynek)
    return (ilejedynek % 2) == 1

def sprpowybraniu(T, N, delwiersz, delkol1, delkol2):
    for wiersz in range(N):
        if wiersz == delwiersz:
            continue
        for kol in range(N):
            if kol == delkol1 or kol == delkol2:
                continue
            if not czy_nieparzysta_l_jed_w_syst_2(T[wiersz][kol]):
                #print(czy_nieparzysta_l_jed_w_syst_2(T[wiersz][kol]))
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

T = [[3,4,4,4],
     [4,3,4,4],
     [4,4,3,4],
     [4,4,4,3]]

#print(czy_nieparzysta_l_jed_w_syst_2(4))

print(czy_usuwanie(T,4))