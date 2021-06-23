def NWD(a,b):
    if b == 0:
        return a
    else:
        return NWD(b,a % b)

def rozbicie(liczba):
    for maska in range(1, 2**len(str(liczba))):
        wyg1 = 0
        wyg2 = 0
        pow10v1 = 1
        pow10v2 = 1
        cliczba = liczba
        while maska > 0:
            #0 pierwsza liczba / 1 druga liczba
            if maska % 2 == 0:
                cyfra = cliczba % 10
                wyg1 += cyfra * pow10v1
                pow10v1 *= 10
            else:
                cyfra = cliczba % 10
                wyg2 += cyfra * pow10v2
                pow10v2 *= 10
            maska //= 2
            cliczba //= 10
        if len(str(wyg1)) + len(str(wyg2)) == len(str(liczba)) and NWD(wyg1,wyg2) == 1:
            print(wyg1, wyg2)


def rozbij(N,A="",B=""):
    if N == "":
        print (A, B)
    else:
        rozbij(N[1:],A+N[0],B)
        rozbij(N[1:],A,B+N[0])
rozbij("21523")