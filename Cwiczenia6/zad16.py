# ord() znak na liczbe
def rekur(slowo, pozycja , sumaascii, iloscsamoglosek, samogloski):
    if pozycja == len(slowo):
        return sumaascii, iloscsamoglosek
    else:
        if slowo[pozycja] in samogloski:
            return rekur(slowo,pozycja + 1, sumaascii + ord(slowo[pozycja]), iloscsamoglosek + 1, samogloski) \
                or rekur(slowo,pozycja +1, sumaascii, iloscsamoglosek, samogloski)
        else:
            return rekur(slowo,pozycja + 1, sumaascii + ord(slowo[pozycja]), iloscsamoglosek , samogloski) \
                or rekur(slowo, pozycja +1, sumaascii, iloscsamoglosek, samogloski)


def wyraz(s1,s2):
    samogloski = ["a", "e", "i", "o", "u", "y"]
    return rekur(s1,0,0,0,samogloski) == rekur(s2,0,0,0,samogloski)

print(wyraz("ula","exe"))