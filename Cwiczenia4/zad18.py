#still not workin
def podconajwsumie(T,N):
    wiersz = kol = 0
    maxsum = 0
    while wiersz < N:
        while kol < N:
            sumapoziom = 0
            sumapion = 0
            y = kol
            while y < N and y - kol <= 10:
                sumapoziom += T[wiersz][y]
                y += 1
            x = wiersz
            while x < N and x - wiersz <= 10:
                sumapion += T[x][kol]
                x += 1

            maxsum = max(sumapion,sumapoziom,maxsum)
            kol += 1
        wiersz += 1
    return maxsum

def podconajwsumiev2(T,N):
    maxsum = 0
    for k in range(N):
        for i in range(N):
            j = i
            sum_v_t = 0
            sum_h_t = 0
            while j < N and j - i <= 10:
                sum_v_t += T[j][k]
                sum_h_t += T[k][j]
                maxsum = max(maxsum, sum_h_t, sum_v_t)
                j += 1
    return maxsum

T1 = [[0,2,2,4],
     [13,0,19,19],
     [8,18,0,22],
     [3,4,14,0]]



print(podconajwsumie(T1,4))
print(podconajwsumiev2(T1,4))