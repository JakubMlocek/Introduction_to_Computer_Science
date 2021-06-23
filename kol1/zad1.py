#Jakub Młocek

def dlczywielokrotny(napis):
    #jezeli dlugosc nieparzysta to nie moze byc sklejeniem dwóch napisów
    N = len(napis)
    for koniec in range(1,N//2+1):
        ilenapisow = N//koniec
        baza = napis[0:koniec]
        for i in range(1,ilenapisow):
            if napis[koniec*i:i*koniec+koniec] != baza:
                return False
        return True


def multi(T):
    max = 0
    for el in T:
        if dlczywielokrotny(el) and len(el) > max:
            max = len(el)
    return max