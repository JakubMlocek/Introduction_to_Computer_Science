def czy_pierwsza(liczba):
    if liczba < 2:
        return False

    i = 2
    while i * i <= liczba:
        if liczba % i == 0:
            return False
        i += 1
    return True

def czy_iloczyn_2_liczb_pierwszych(liczba):
    for l1 in range(liczba + 1):
        if not czy_pierwsza(l1):
            continue
        for l2 in range(liczba + 1):
            if not czy_pierwsza(l2):
                continue
            if l1 * l2 == liczba:
                return True
    return False


def czy_wycinek(T1, T2, N):
    for poczwycinku1 in range(N):
        for poczwycinku2 in range(N):
            for dlwycinku in range(24 + 1):
                if poczwycinku1 + dlwycinku > N:
                    continue
                if poczwycinku2 + (24-dlwycinku) > N:
                    continue

                temp1 = T1[poczwycinku1:dlwycinku]
                temp2 = T2[poczwycinku2:24-dlwycinku]

                sum1 = sum2 = 0
                for el in temp1:
                    sum1 += el
                for el in temp2:
                    sum2 += el

                if czy_iloczyn_2_liczb_pierwszych(sum1 + sum2):
                    return True
    return False



