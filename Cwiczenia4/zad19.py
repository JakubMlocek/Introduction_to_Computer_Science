def zlicz(tablica, iloczyn):
    ruchy = [[1, -2] , [2, -1], [2, 1], [1,2]] #nie robimy ruchow w gore bo powtarzalibysmy sie
    counter = 0
    n = len(tablica)
    for w in range(n):
        for k in range(n):
            if tablica[w][k] != 0 and iloczyn % tablica[w][k] == 0:
                for i in range(4):
                    wiersz = w + ruchy[i][0]
                    kolumna = k + ruchy[i][1]
                    if 0 <= wiersz < n and 0 <= kolumna < n:
                        if tablica[w][k] * tablica[wiersz][kolumna] == iloczyn:
                            counter += 1
    return counter


T =[[1,2,3,4],
    [2,3,4,1],
    [0,1,20,18],
    [11,11,11,11]]
iloczyn = 11
print(zlicz(T,iloczyn))