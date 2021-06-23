def isgrowingstr(sequence):
    for i in range(1, len(sequence)):
        if sequence[i-1] >= sequence[i]:
            return False
    return True

def isgrowingint(sequence):
    prev = 10 #wieksze od cyfr
    while sequence > 0:
        if sequence % 10 >= prev:
            return False
        prev = sequence % 10
        sequence //= 10
    return True



liczba = input("Liczba:  ")
print(isgrowingstr(liczba))
print(isgrowingint(int(liczba)))