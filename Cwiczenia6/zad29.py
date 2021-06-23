def podzbiór(T, r, m = 0, cntr = [0, 0, 0], pos = 0):
    if (cntr[0] ** 2 + cntr[1] ** 2 + cntr[2] ** 2) ** 0.5 <= r and m >= 3:
        return True
    if pos == len(T):
        return False
    for i in range(3):
    return podzbiór(T, r, m + 1, [(cntr[0]*m + T[pos][0])/(m + 1), \
                                  (cntr[1]*m + T[pos][1])/(m + 1), \
                                  (cntr[2]*m + T[pos][2])/(m + 1)], \
                                   pos + 1) \
           or podzbiór(T, r, m, cntr, pos + 1)


r = 9
T = [(1, 2, 3), (15, 13, 11), (4, 5, 6), (7, 8, 9)]

print(podzbiór(T, r))