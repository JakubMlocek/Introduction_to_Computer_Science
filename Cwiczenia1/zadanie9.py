podzielnik = 1

liczba = 16

while(podzielnik**2 <= liczba):
    if liczba % podzielnik == 0:
        print(podzielnik)
        if(podzielnik != liczba/podzielnik):
            print(liczba//podzielnik)
    podzielnik += 1

#1
#2
#3
#6
