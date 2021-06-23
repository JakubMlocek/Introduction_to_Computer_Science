def NWD(a,b):
    if b == 0:
        return a
    else:
        return NWD(b, a % b)

def NWW(a,b):
    return a*b//NWD(a,b)

def dodaj(l1, l2):
    if l1[1] == l2[1]:
        return(l1[0] + l2[0],l1[1])
    else:
        licznik1 = l1[0]
        licznik2 = l2[0]
        nowymianownik = NWW(l1[1],l2[1])
        licznik1 *= nowymianownik//l1[1]
        licznik2 *= nowymianownik//l2[1]
        return (licznik1+licznik2,nowymianownik)

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

def pomnoz(l1, l2):
    return(l1[0]*l2[0],l1[1]*l2[1])

def podziel(l1, l2):
    return(l1[0]*l2[1],l1[1]*l2[0])

def potega(l, ktora):
    if ktora == 0:
        return (1,1)
    licznik = 1
    mianownik = 1

    for i in range(abs(ktora)):
        licznik *= l[0]
        mianownik *= l[1]

    if ktora > 0:
        return (licznik, mianownik)
    else:
        return (mianownik,licznik)

def skroc(l):
    return (l[0]//NWD(l[0],l[1]),l[1]//NWD(l[0],l[1]))

#liczby wymierne w krotkach (l,m) postaci (licznik, mianownik)
def wypisz(l):
    print(f"{l[0]}/{l[1]}")

def wczytaj():
    licznik = int(input("Podaj licznik>>"))
    mianownik = int(input("Podaj mianownik>>"))
    return (licznik,mianownik)

x1, y1, z1 = (1,1),(1,1),(1,1)
x2, y2, z2 = (1,1),(-1,1),(1,1)

wsp1 = [x1,y1,z1]
wsp2 = [x2,y2,z2]

#METODA WYZNACNZIKOW
W = odejmij(pomnoz(wsp1[0],wsp2[1]),pomnoz(wsp2[0],wsp1[1]))
Wy = odejmij(pomnoz(wsp1[0],wsp2[2]),pomnoz(wsp2[0],wsp1[2]))
Wx = odejmij(pomnoz(wsp1[2],wsp2[1]),pomnoz(wsp2[2],wsp1[1]))

if W != 0:
    wypisz(podziel(Wx,W))
    wypisz(podziel(Wy,W))
elif W == 0 and Wx == 0 and Wy == 0:
    print("ukl nieoznaczony")
else:
    print("ukl sprzeczny")