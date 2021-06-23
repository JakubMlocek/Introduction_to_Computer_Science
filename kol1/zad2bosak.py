#Piotr Bosak
#szukamy najwiekszej i najmniejszej liczby binarnej (najwiecej/najmniej jedynek z przodu)

def max(T):
    n = len(T)
    kolumna = n
    wiersz = n
    for i in range(n):
        for j in range(n):
            if T[i][j]==1:
                if j < kolumna:
                    kolumna = j
                    wiersz = i
                elif j == kolumna:
                    for k in range(j,n):
                        if T[i][k] ==1 and T[wiersz][k] != 1:
                            wiersz = i
    return wiersz

def min(T):
    n = len(T)
    kolumna = 0
    wiersz = 0
    i = j = n-1
    while i >= 0:
        while j >=0:
            if T[i][j]==0:
                if j > kolumna:
                    kolumna = j
                    wiersz = i
                elif j == kolumna:
                    k = j
                    while k >=0:
                        if T[i][k] ==0 and T[wiersz][k] != 0:
                            wiersz = i
                        k -= 1
            j -=1
        i -=1
    return wiersz


def distance(T):
    return abs(max(T)-min(T))



