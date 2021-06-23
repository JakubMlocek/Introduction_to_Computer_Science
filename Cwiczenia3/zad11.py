import random

def najdlpodciaggeo(tab):
    najdlpodc = []
    for poczatek in range(len(tab)-1):
        q = tab[poczatek + 1] / tab[poczatek]
        print("q: " + str(q))
        for koniec in range(poczatek + 1, len(tab)):
            print(tab[koniec] / tab[koniec - 1])
            if tab[koniec] / tab[koniec - 1] == q:
                if koniec - poczatek + 1 > len(najdlpodc):
                    najdlpodc = tab[poczatek:koniec+1]
            else:
                break
    return najdlpodc

#N = int(input("N:  "))
#tab = [random.randint(1,1000) for i in range(N)]
#print(tab)
#print(najdlpodciaggeo(tab))
tab = [1, 8, 3, 9, 27, 9 ,11, 12]
print(najdlpodciaggeo(tab))