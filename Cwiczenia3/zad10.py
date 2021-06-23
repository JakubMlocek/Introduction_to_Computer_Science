import random

def najdlpodciagaryt(tab):
    najdlpodc = []
    for poczatek in range(len(tab)-1):
        r = tab[poczatek + 1] - tab[poczatek]
        for koniec in range(poczatek + 1, len(tab)):
            if tab[koniec] - tab[koniec - 1] == r:
                if koniec - poczatek + 1 > len(najdlpodc):
                    najdlpodc = tab[poczatek:koniec+1]
            else:
                break
    return najdlpodc

N = int(input("N:  "))
tab = [random.randint(1,1000) for i in range(N)]
print(tab)
#print(najdlpodciagaryt(tab))
tab = [1, 8, 3, 5, 7, 9 ,11, 12]
print(najdlpodciagaryt(tab))