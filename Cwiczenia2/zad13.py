def islastunique(liczba):
    return not liczba[-1] in liczba[:-1]

liczba = input("L:  ")
print(islastunique(liczba))