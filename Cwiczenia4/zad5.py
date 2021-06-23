def sumaelementowwiersza(T,N,wiersz):
    sum = 0
    for i in range(N):
        sum += T[wiersz][i]
    return sum

def sumaelementowkol(T,N,kol):
    sum = 0
    for i in range(N):
        sum += T[i][kol]
    return sum

def zworckordy(T, N):
    max = (0,0)
    maxiloraz = 0
    for x in range(N):
        for y in range(N):
            try:
                if sumaelementowkol(T, N, y) / sumaelementowwiersza(T, N, x) > maxiloraz:
                    maxiloraz = sumaelementowkol(T, N, y) / sumaelementowwiersza(T, N, x)
                    max = (x, y)
            except:
                pass
    return max


T = [[2, 32, 12], [1, 2, 3], [45, 57, 89]]
for i in T:
    print(i)
print(zworckordy(T,3))