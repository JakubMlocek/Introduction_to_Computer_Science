from math import log10
from math import floor

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**(1/2))+1, 2):
        if n % i == 0:
            return False
    return True

liczby = {}
def rekur(n):
    if n == 0:
        return False
    global liczby
    dl = floor(log10(n)) + 1 #dlugosc liczby
    if dl < 2:
        return False
    if is_prime(n):
        liczby[n] = True
    for i in range(dl):
        #1234 % 10 = 4
        #1234 // 100 = 12
        # 12, 4 = 124
        prawa = n % (10 ** i)
        lewa = n // (10**(i+1))
        nowe_n = lewa * (10**i) + prawa
        rekur(nowe_n)

rekur(2137)
for klucz, wartosc in liczby.items():
    print(klucz)