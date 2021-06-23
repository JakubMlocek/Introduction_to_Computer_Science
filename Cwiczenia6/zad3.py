def ruch_krola(T, wiersz, kol, koszt = 0):
    global min_cost
    koszt += T[wiersz][kolumna]
    if wiersz == 7:
        if min_cost == None or koszt < min_cost:
            min_cost = koszt
    else:
        if 0 < kol < 7:
            return ruch_krola(T, wiersz + 1, kol, koszt) \
            or ruch_krola(T, wiersz + 1, kol + 1, koszt) \
            or ruch_krola(T, wiersz + 1, kol - 1, koszt)
        elif kol == 0:
            return ruch_krola(T, wiersz + 1, kol + 1, koszt) \
            or ruch_krola(T, wiersz + 1, kol, koszt)
        if kol == 7:
            return ruch_krola(T, wiersz + 1, kol - 1, koszt) \
            or ruch_krola(T, wiersz + 1, kol, koszt)

T = [[0,1,2,3,4,5,6,7,8],
     [0,1,2,3,4,5,6,7,8],
     [0,1,2,3,4,5,6,7,8],
     [0,1,2,3,4,5,6,7,8],
     [0,1,2,3,4,5,6,7,8],
     [0,1,2,3,4,5,6,7,8],
     [0,1,2,3,4,5,6,7,8],
     [0,1,2,3,4,5,6,7,8]]

min_cost = None
ruch_krola(T,0,3,0)