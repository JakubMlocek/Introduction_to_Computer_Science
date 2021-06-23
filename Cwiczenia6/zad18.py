from math import log10
from math import floor
from random import randint

def warunek(a,b):
    ostatniacyfraa = a % 10
    dlb = floor(log10(b)) + 1
    pierwszacyfrab = b//10**(dlb - 1)
    return ostatniacyfraa < pierwszacyfrab

def krol(pozx = 0, pozy = 0):
    global T
    if pozx == pozy == 7:
        return True
    else:
        kierx = [1,1,0]
        kiery = [0,1,-1]
        for i in range(3):
            newx = pozx + kierx[i]
            newy = pozy + kiery[i]
            if newx > 7 or newx < 0:
                continue
            if newy > 7 or newy < 0:
                continue
            if warunek(T[pozy][pozx],T[newy][newx]):
                return krol(newx,newy)

T = [[8,7,6,5,4,3,2,1],
    [8,7,6,5,4,3,2,1],
    [8,7,6,5,4,3,2,1],
    [8,7,6,5,4,3,2,1],
    [8,7,6,5,4,3,2,1],
    [8,7,6,5,4,3,2,1],
    [8,7,6,5,4,3,2,1],
    [8,7,6,5,4,3,2,1]]



print(krol(0,0))
