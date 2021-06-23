def czywylnieparzyste(liczba):
    while liczba > 0:
        if (liczba % 10) % 2 == 0:
            return False
        liczba //= 10
    return True

def czywwierszu(T, N):
    for i in range(N):
        czywiersz = False
        for j in range(N):
            if czywylnieparzyste(T[i][j]):
                czywiersz = True
        if czywiersz == False:
            return False
    return True

T = [[2,32,11],[1,2,3],[45,57,89]]
print(czywwierszu(T,3))

