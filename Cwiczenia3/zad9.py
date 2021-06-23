import random

def najdlpodciagrosnacy(tab):
    max = 0
    sum = 1
    najdlpodc = []
    for poczatek in range(len(tab) - 1):
        if tab[poczatek + 1] > tab[poczatek]:
            #dokoncz!

    return najdlpodc

N = int(input("N:  "))
tab = [random.randint(1,1000) for i in range(N)]
print(tab)
print(najdlpodciagrosnacy(tab))
