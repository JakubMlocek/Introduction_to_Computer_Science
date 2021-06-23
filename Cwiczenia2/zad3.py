"""
def czypalindrom(liczba):
    for i in range(int(len(liczba)/2)):
        if liczba[i] != liczba[len(liczba)-1-i]:
            return False
    return True

def dec2bin(liczba):
    liczba = int(liczba)
    wynik = ""
    while(liczba > 1):
        #print(int(liczba % 2))
        wynik += str(int(liczba % 2))
        liczba /= 2
    return wynik

liczba = input("Podaj Liczbe:  \n")
print(liczba)
print(czypalindrom(liczba))
print(dec2bin(liczba))
print(czypalindrom(dec2bin(liczba)))
"""
#inne podejscie
def ilecyfrwliczbie(liczba):
    ile = 0
    while liczba > 0:
        liczba //= 10
        ile += 1
    return ile

def rewers(liczba):
    rew = 0
    #miejsce = 10**(ilecyfrwliczbie(liczba)-1)
    while liczba > 0:
        rew = rew * 10 + (liczba % 10)
        #rew += (liczba%10) * miejsce
        liczba //= 10
        #miejsce //= 10
    return rew

def rewersbin(liczba):
    rew = 0
    while liczba > 0:
        rew = rew * 2 + (liczba % 2)
        print(rew)
        liczba //= 2
    return rew

print(rewers(123))
print(rewersbin(123))