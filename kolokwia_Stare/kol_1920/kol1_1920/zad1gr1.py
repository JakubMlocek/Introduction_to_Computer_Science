from random import randint
def czy_conajmniej_druga_pot_l_nat(suma):
    podstawa = 2
    sprsuma = podstawa * podstawa
    while sprsuma <= suma:
        if sprsuma > suma:
            return False
        while sprsuma <= suma:
            if sprsuma == suma:
                return True
            sprsuma *= podstawa
        podstawa += 1
        sprsuma = podstawa * podstawa
    return False

def czy_wycinek(T1, T2, N):
    for poczwycinka1 in range(N):
        for poczwycinka2 in range(N):
            for podzialdlwycinka in range(24+1):
                if N - poczwycinka1 - podzialdlwycinka < 0:
                    continue
                if N - 24 - poczwycinka2 + podzialdlwycinka < 0:
                    continue
                temp1 = T1[poczwycinka1:podzialdlwycinka]
                temp2 = T2[poczwycinka2:24-podzialdlwycinka]
                sum1 = 0
                sum2 = 0
                for el in temp1:
                    sum1 += el
                for el in temp2:
                    sum2 += el
                if czy_conajmniej_druga_pot_l_nat(sum1 + sum2):
                    #print(poczwycinka1)
                    #print(poczwycinka2)
                    #print(podzialdlwycinka)
                    return True
    return False

N = 30
T1 = [randint(0,100) for _ in range(N)]
T2 = [randint(0,100) for _ in range(N)]
print(T1)
print(T2)
print(czy_wycinek(T1,T2,N))

