wszystkie_nki = []
def uniqe_tab(tab):
    uq = []
    for x in tab:
        if x not in uq:
            uq.append(x)
    return uq

def licz_nki(tab, iloczyn, n, nki = [], pozycja = 0):
    global wszystkie_nki
    if n == 1:
        for i in range(pozycja,len(tab)):
            if tab[i] == iloczyn:
                nki.append(tab[i])
                wszystkie_nki.append(sorted(nki))
    else:
        for i in range(pozycja,len(tab)):
            if iloczyn % tab[i] == 0:
                licz_nki(tab, iloczyn // tab[i], n - 1, nki + [tab[i]], pozycja + 1)

T = [4,5,6,1,2,3,8]
licz_nki(T,24,3)
print(len(uniqe_tab(wszystkie_nki)))

