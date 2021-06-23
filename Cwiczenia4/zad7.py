def znajdz_najmniejszy(indexy, T1, N):
    min_wart = 1e10 #max = None
    for i in range(N):
        if indexy[i] < N:
            if T1[i][indexy[i]] < min_wart:
                min_wart = T1[i][indexy[i]]
    return min_wart

def wypelnij_T2(T1,T2, N):
    indexy = [0] * N
    i = 0
    while i < N**2:
        v = znajdz_najmniejszy(indexy, T1, N)
        t = 0
        while t < N:
            if indexy[t] < N and T1[t][indexy[t]] == v:
                T2[i] = v
                indexy[t] += 1
                i += 1
            else:
                t += 1



N = 4
#T1 = [ [0] * N for i in range(N) ]
T1 = [[1,2,2,4],[13,17,19,19],[8,18,18,22],[3,4,14,20]]
T2 = [0] * N**2

pozycjaT2 = 0
for p in range(N**2):
    minwwierszu = 0
    min = 9999999999
    for wiersz in range(N):
        try:
            if T1[wiersz][0] < min:
                minwwierszu = wiersz
                min = T1[wiersz][0]
        except:
            continue

    T2[pozycjaT2] = min
    pozycjaT2 += 1
    T1[minwwierszu] = T1[minwwierszu][1:]



print(T1)
print(T2)