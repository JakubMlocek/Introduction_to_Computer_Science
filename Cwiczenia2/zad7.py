def ciag(n):
    return n * n + n + 1

def isCase(liczba):
    n = 1
    while ciag(n) < liczba:
        if liczba % ciag(n) == 0:
            return True
        n += 1
    return  False

liczba = int(input("liczba:  "))
print(isCase(liczba))