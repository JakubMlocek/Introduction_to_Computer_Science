def najdlcgeo(T, N):
    dl = maksdl = 1
    poprzq = T[0][0] / T[1][1]
    for i in range(N-1):
        q = T[i][i] / T[i+1][i+1]
        print(q)
        if q == poprzq:
            dl += 1
            if dl > maksdl:
                maksdl = dl
        else:
            if dl > maksdl:
                maksdl = dl
            dl = 1
            poprzq = q

    if maksdl >= 3:
        return (True, maksdl)
    else:
        return (False, maksdl)


T = [[1,2,2,4],
     [13,3,19,19],
     [8,18,9,22],
     [3,4,14,5]]

print(najdlcgeo(T,4))