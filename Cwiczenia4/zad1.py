N = 7
T = [0] * N
for i in range(N):
    T[i] = [0] * N

#tab = [[0] * N for i in range(N)]
#print(tab)
aktualnaliczba = 1
wiersz = 0
kol = 0
zajetyzakres = 0
while N - zajetyzakres > 0:
    for i in T:
        print(i)
    print()
    #idziemy w prawo
    while kol < N - zajetyzakres:
        T[wiersz][kol] = aktualnaliczba
        aktualnaliczba += 1
        kol += 1
    kol -= 1
    #idziemy w dół
    wiersz += 1
    while wiersz < N - zajetyzakres:
        T[wiersz][kol] = aktualnaliczba
        aktualnaliczba += 1
        wiersz += 1
    wiersz -= 1
    #idziemy w lewo
    kol -= 1
    while kol >= zajetyzakres:
        T[wiersz][kol] = aktualnaliczba
        aktualnaliczba += 1
        kol -= 1
    kol += 1

    zajetyzakres += 1 #zmniejszamy tablice po ktorej chodzimy
    #idziemy w gore
    wiersz -= 1
    while wiersz > zajetyzakres:
        T[wiersz][kol] = aktualnaliczba
        aktualnaliczba += 1
        wiersz -= 1



for i in T:
    print(i)

