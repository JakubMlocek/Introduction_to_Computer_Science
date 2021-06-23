def ileparzwpiatkowym(l):
    ile = 0
    while l > 0:
        cyfra = l % 5
        if cyfra % 2 == 0:
            ile += 1
        l //= 5
    return ile


def is_correct_5(l1, l2):
    return ileparzwpiatkowym(l1) == ileparzwpiatkowym(l2)


def is_possible(T1, T2, N1, N2):
    for w in range(-N1+1,N2):
        for k in range(-N1+1,N2):
            licznikpol = 0
            licznikzgodnosci = 0
            for y in range(w,w+N1):
                for x in range(k,k+N1):
                    if(y>=0 and y<N2 and x>=0 and x<N2):
                        licznikpol+=1
                        if(is_correct_5(T1[y-w][x-k],T2[y][x])):
                            licznikzgodnosci+=1
            if(licznikzgodnosci/licznikpol>0.33):
                return True
    return False

