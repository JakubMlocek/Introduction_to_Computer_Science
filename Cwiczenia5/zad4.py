def odejmij(l1, l2):
    if l1[1] == l2[1]:
        return(l1[0] - l2[0],l1[1])
    else:
        licznik1 = l1[0]
        licznik2 = l2[0]
        nowymianownik = NWW(l1[1],l2[1])
        licznik1 *= nowymianownik//l1[1]
        licznik2 *= nowymianownik//l2[1]
        return (licznik1-licznik2,nowymianownik)

def podziel(l1, l2):
    return(l1[0]*l2[1],l1[1]*l2[0])

def skroc(l):
    return (l[0]//NWD(l[0],l[1]),l[1]//NWD(l[0],l[1]))

def czyrowne(l1, l2):
    l1 = skroc(l1)
    l2 = skroc(l2)

    if l1[0] == l2[0] and l1[1] == l2[1]:
        return True
    else:
        return False


def CaCg(T,N):
    LA = 0
    LG = 0
    dla = 1
    dlg = 1
    czya = False
    r = None
    czyg = False
    q = None
    for i in range(N-1):
        if czya:
            if czyrowne(odejmij(T[i+1],T[i]),r):
                dla += 1
            else:
                if dla > 2:
                    LA += 1
                czya = False
                dla = 1
        else:
            r = odejmij(T[i+1],T[i])
            dla ++

        if czyg:
            if czyrowne(podziel(T[i+1],T[i]),q):
                dlg += 1
            else:
                if dlg > 2:
                    LB += 1
                czyg = False
                dlg = 1
        else:
            q = podziel(T[i+1],T[i])
            dlg += 1

    if LA > LG:
        return 1
    elif LA < LG:
        return -1
    else:
        return 0

