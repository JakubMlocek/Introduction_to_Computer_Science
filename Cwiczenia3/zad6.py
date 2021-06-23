def czyelementconajmniej1nieparzysta(liczba):
    while liczba > 0:
        cyfra = liczba % 10
        if cyfra % 2 == 1:
            return True
        liczba //= 10
    return False

import random
N = int(input("N:  "))

tab = [random.randint(1,1000) for i in range(N)]

for liczba in tab:
    if not czyelementconajmniej1nieparzysta(liczba):
        print("NIE!")
        break