def czyhetmanybezszacha(pozycje):
    N = 100
    ilosc_hetmanow = len(pozycje)
    wiersze = [False for _ in range(N)]
    kolumny = [False for _ in range(N)]
    przekNE = [False for _ in range(2*N-1)]
    przekSW = [False for _ in range(2*N-1)] #liczba przek w jedna str 2n-1

    for i in range(ilosc_hetmanow):
        w, k = pozycje(i)
        if wiersze[w] == True or kolumny[k] == True:
            return False
        if przekNE[w+k] == 1 or przekSW[w-k+N-1] == 1: #w-k+N-1 aby nie wyszło za tab
            return False
        wiersz[w] = True
        kolumny[k] = True
        wiersz[w] = True
        wiersz[w] = True
        przekNE[w + k] = 1
        przekSW[w - k + N - 1] = 1
    return True



#ponizej wersja bez optymalizacji
def szachujwiersz(czypoleszachowane, pozycja):
    for i in range(100):
        if czypoleszachowane[pozycja[0]][i] == False:
            return False
    czypoleszachowane[pozycja[0]] = [False for _ in range(100)]
    return True

def szachujkolumne(czypoleszachowane, pozycja):
    for i in range(100):
        if czypoleszachowane[i][pozycja[1]] == False:
            return False
        else:
            czypoleszachowane[i][pozycja[1]] = False
            return True

def szachujskosprawo(czypoleszachowane, pozycja):
    i = 0
    while i + pozycja[0] < 100 and i + pozycja[1] < 100:
        if czypoleszachowane[pozycja[0]+i][pozycja[1]+i] == False:
            return False
        czypoleszachowane[pozycja[0]+i][pozycja[1]+i] = False
        i+=1
    return True

def szachujskoslewo(czypoleszachowane, pozycja):
    i = 0
    while pozycja[0] - i > 0 and pozycja[1] - i > 0:
        if czypoleszachowane[pozycja[0]-i][pozycja[1]-i] == False:
            return False
        czypoleszachowane[pozycja[0]-i][pozycja[1]-i] = False
        i+=1
    return True

def czyhetmanybezszachowania(T,pozycje):
    iloschetmanow = len(pozycje)
    czypoleszachowane =[[False for j in range(100)] for i in range(100)]
    for pozycja in pozycje:
        if not szachujkolumne(czypoleszachowane,pozycja):
            return False
        if not szachujwiersz(czypoleszachowane,pozycja):
            return False
        if not szachujskoslewo(czypoleszachowane,pozycja):
            return False
        if not szachujskosprawo(czypoleszachowane,pozycja):
            return False
    return True


