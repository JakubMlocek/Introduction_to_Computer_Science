def czyjednaparzysta(liczba):
    while liczba > 0:
        if (liczba % 10) % 2 == 0:
            return True
        liczba //= 10
    return False

def czywwierszu(T, N):
    for i in range(N):
        czywiersz = True
        for j in range(N):
            if not czyjednaparzysta(T[i][j]):
                czywiersz = False
        if czywiersz == True:
            return True
    return False

T = [[2,32,12],[1,2,3],[45,57,89]]
print(czywwierszu(T,3))

