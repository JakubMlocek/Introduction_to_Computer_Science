def skoczek(T, pozx, pozy):
    T[pozy][pozx] = True
    kierx = [1,2,2,1,-1,-2,-2,-1]
    kiery = [-2,-1,1,2,2,1,-1,-2]
    for i in range(8):
        newx = pozx + kierx[i]
        newy = pozy + kiery[i]
        if newx < 0 or newx >= len(T):
            continue
        if newy < 0 or newy >= len(T):
            continue
        return skoczek(T, newy, newx)

T = [[False, False, False, False],
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False]]

skoczek(T,1,0)

print(T)