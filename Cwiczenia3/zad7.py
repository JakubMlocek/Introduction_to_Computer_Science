def czyelementtylkonieparzyste(liczba):
    while liczba > 0:
        cyfra = liczba % 10
        if cyfra % 2 == 0:
            return False
        liczba //= 10
    return True

import random
N = int(input("N:  "))

tab = [random.randint(1,1000) for i in range(N)]

for liczba in tab:
    if czyelementtylkonieparzyste(liczba):
        print("Tak!")
        break