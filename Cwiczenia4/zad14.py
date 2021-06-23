def czyzgodne(l1, l2):
    iljedynek1 = 0
    while l1 > 0:
        if l1 % 2 == 1:
            iljedynek1 += 1
        l1 //= 2

    iljedynek2 = 0
    while l2 > 0:
        if l2 % 2 == 1:
            iljedynek2 += 1
        l2 //= 2

    return iljedynek1 == iljedynek2

def czyzgodnepolozenie(T1, N1, T2, N2):
    if N1 > N2:
        return False
    wiersz = kol = 0
    while wiersz + N1 - 1 < N2:
        while kol + N1 - 1 < N2:
            ilezgodnych = 0
            for y in range(N1):
                for x in range(N1):
                    if czyzgodne(T1[wiersz+y][kol+x],T2[wiersz+y][kol+x]):
                        ilezgodnych += 1
            if ilezgodnych/(N1**2) >= (1/3):
                return True
            kol += 1
        wiersz += 1
    return False


T1 = [[0,2,2,4],
     [13,0,19,19],
     [8,18,0,22],
     [3,4,14,0]]

T2 = [[0,2,2,4],
     [13,0,19,19],
     [8,18,0,22],
     [3,4,14,0]]

print(czyzgodnepolozenie(T1,4,T2,4))