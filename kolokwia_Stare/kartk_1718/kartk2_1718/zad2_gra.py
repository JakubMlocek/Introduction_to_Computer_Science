def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i+=1
    return True

rozmieszczenia  = []
def wypelnij(T, poz = 1):
    if poz == 9:
        rozmieszczenia.append(T)
    else:
        for el in range(1, 10):
            if el not in T:
                if abs(T[poz - 1] - el) >= 2 and not(is_prime(T[poz - 1]) and is_prime(el)):
                    T_cpy = T[:]
                    T_cpy[poz] = el
                    wypelnij(T_cpy,poz + 1)


T = [1,0,0,0,0,0,0,0,0]
wypelnij(T)
for line in rozmieszczenia:
    print(line)
print(len(rozmieszczenia))