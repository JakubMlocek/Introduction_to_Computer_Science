def czyprzyjaciolki(liczba1, liczba2):
    cyfry1 = [0]*10
    while liczba1 > 0:
        cyfry1[liczba1 % 10] += 1
        liczba1 //= 10
    cyfry2 = [0]*10
    while liczba2 > 0:
        cyfry2[liczba2 % 10] += 1
        liczba2 //= 10

    for i in range(10):
        if (cyfry1[i] != 0 and cyfry2[i] == 0) or (cyfry1[i] == 0 and cyfry2[i] != 0):
            return False
    return True

def sasiedziprzyjaciolki(T, N,x,y):
    kierx = [0,1,0,-1]
    kiery = [1,0,-1,0]

    ileprzyj = 0
    for i in range(4):
        newx = x + kierx[i]
        newy = y + kiery[i]

        if newx < 0 or newx >= N:
            continue
        if newy < 0 or newy >= N:
            continue
            
        if not (czyprzyjaciolki(T[x][y],T[newx][newy])):
            return False
    return True

def sprdlawszystkich(T,N):
    counter = 0
    for i in range(N):
        for j in range(N):
            if sasiedziprzyjaciolki(T,N,i,j):
                counter += 1
    return counter