#dodatek
def generatordwutrzypiatkowych(zakres):
    #zwraca ile w danym zakresie
    counter = 0
    m2 = 1
    while m2 <= zakres:
        m3 = m2
        while m3 <= zakres:
            m5 = m3
            while m5 <= zakres:
                counter += 1
                m5 *= 5
            m3 *= 3
        m2 *= 2
    return counter



#normalne rozwiazanie
def czydwutrzypiatkowa(liczba):
    dzielnik = 2
    while liczba > 1:
        if liczba % dzielnik == 0:
            liczba /= dzielnik
            if dzielnik != 2 and dzielnik != 3 and dzielnik != 5:
                return False
        else:
            dzielnik += 1
    return True

N = 20

counter = 0

for i in range(1, N+1):
    if czydwutrzypiatkowa(i):
        counter += 1

print(counter)
print(generatordwutrzypiatkowych(20))




