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


print(dodaj((3,4),(5,3)))
print(odejmij((3,4),(5,3)))
print(pomnoz((3,4),(5,3)))
print(podziel((3,4),(5,3)))
print(potega((3,4),(-3)))
print(skroc((12,36)))
