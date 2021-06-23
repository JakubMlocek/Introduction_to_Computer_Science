def podzbior(T, suma, wiersz, zajetekol = [True]*8):
    if suma == 0:
        return True
    if wiersz == len(T):
        return False
    for kol in range(8):
        if zajetekol[kol]:
            zajetekol[kol] = False
            return podzbior(T,suma - T[wiersz][kol], wiersz + 1, zajetekol)
    return pozbior(T, suma, wiersz + 1, zajetekol)

T = [[1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8]]

print(podzbior(T,36,0))


