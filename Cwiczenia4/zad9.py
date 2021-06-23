def iloczynpolnaroznych(T,wiersz, kolumna, dlboku):
    dlboku -= 1
    iloczyn = 1
    iloczyn *= T[wiersz][kolumna]
    iloczyn *= T[wiersz + dlboku][kolumna]
    iloczyn *= T[wiersz][kolumna + dlboku]
    iloczyn *= T[wiersz + dlboku][kolumna + dlboku]
    return iloczyn

def szukajkwadrat(T, N, k):
    wiersz = kol = 0
    dlboku = 3
    while dlboku <= N:
        while wiersz + dlboku < N:
            while kol + dlboku < N:
                if iloczynpolnaroznych(T, wiersz, kol, dlboku) == k:
                    return (True, (wiersz + dlboku) // 2, (kol + dlboku)//2)
        dlboku += 2
    return False, None, None

T = [[1,2,2,4],
     [13,3,19,19],
     [8,18,9,22],
     [3,4,14,5]]

print(szukajkwadrat(T,4,144))
