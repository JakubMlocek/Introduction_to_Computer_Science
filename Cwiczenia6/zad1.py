def czypierwsza(liczba):
    if liczba < 2 or (liczba % 2 == 0 and liczba != 2):
        return False
    i = 3
    while i*i <= liczba:
        if liczba % i == 0:
            return False
        i += 2
    return True


def zwroccyfryliczby(liczba):
    cyfry = []
    while liczba > 0:
        cyfry.append(liczba % 10)
        liczba //= 10
    return cyfry[::-1]

print(zwroccyfryliczby(2137))

def tworzliczby(liczba, cyfry, element = 0):
    if element == len(cyfry):
        if czypierwsza(liczba) and len(str(liczba)) >= 2:
            print(liczba)
        else:
            pass
    else:
        if czypierwsza(liczba) and len(str(liczba)) >= 2:
            print(liczba)
            print()
        return tworzliczby(liczba*10+cyfry[element], cyfry, element + 1) or tworzliczby(liczba,cyfry,element + 1)

liczba = 2137
print(tworzliczby(0,zwroccyfryliczby(liczba)))

