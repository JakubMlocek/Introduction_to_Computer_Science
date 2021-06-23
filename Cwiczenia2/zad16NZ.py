def sumacyfrliczby(liczba):
    sum = 0
    while liczba > 0:
        sum += (liczba % 10)
        liczba //= 10
    return sum

def sumawrozkladzie(liczba):
    sum = 0
    dzielnik = 2
    czydodac = False
    while liczba > 1:
        if liczba % dzielnik == 0:
            liczba //= dzielnik
            if not czydodac:
                sum += dzielnik
            czydodac = False
        else:
            czydodac = True
            dzielnik += 1
    return sum


print(sumawrozkladzie(85))