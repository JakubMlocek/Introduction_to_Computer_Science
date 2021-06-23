def waga(liczba):
    ile_roz_czyn_pierw = 0
    czynnik = 2
    while liczba > 1:
        if liczba % czynnik == 0:
            ile_roz_czyn_pierw += 1
            while liczba % czynnik == 0:
                liczba //= czynnik
        czynnik += 1
    return ile_roz_czyn_pierw


def podzialtabna3podzbioryorownychwagach(tab, p1 = 0, p2 = 0, p3 = 0, dodawany_element = 0):
    if dodawany_element == len(tab):
        return p1 == p2 == p3
    else:
        return podzialtabna3podzbioryorownychwagach(tab,p1 + waga(tab[dodawany_element]),p2 ,p3, dodawany_element + 1) \
               or podzialtabna3podzbioryorownychwagach(tab,p1 ,p2 + waga(tab[dodawany_element]) ,p3, dodawany_element + 1) \
               or podzialtabna3podzbioryorownychwagach(tab,p1 ,p2 ,p3  + waga(tab[dodawany_element]), dodawany_element + 1)


#wersja 2
def podzialtabna3podzbioryorownychwagach(tab, p1 = 0, p2 = 0, p3 = 0):
    if len(tab) == 0:
        return p1 == p2 == p3
    else:
        return podzialtabna3podzbioryorownychwagach(tab[1:],p1 + waga(tab[0]),p2 ,p3) \
               or podzialtabna3podzbioryorownychwagach(tab[1:],p1 ,p2 + waga(tab[0]) ,p3) \
               or podzialtabna3podzbioryorownychwagach(tab[1:],p1 ,p2 ,p3  + waga(tab[0]))


l = [1,2,6,30,64]

print(podzialtabna3podzbioryorownychwagach(l))