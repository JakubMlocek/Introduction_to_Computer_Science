def czypustysrodek(l1, l2, l3, l4, wsp):
    for el in wsp:
        if  l1[0] < el[0] < l2[0]:
            return False
        if  l2[1] < el[1] < l3[1]:
            return False
    return True

def czykwadratbezwnetrza(wsp):
    N = len(wsp)
    for pierwszy in range(wsp):
        for drugi in range(pierwszy + 1,wsp): #ta sama y co pierwszy
            if wsp[pierwszy][1] != wsp[drugi][1]:
                continue
            for trzeci in range(drugi + 1, wsp):#ta sama x co drugi i wys co szer
                if wsp[drugi][0] != wsp[trzeci][0] or (abs(wsp[trzeci][1] - wsp[drugi][1]) != abs(wsp[drugi][0] - wsp[pierwszy][0]):
                    continue
                for czwarty in range(trzeci + 1, wsp): #x jak pierwszy i y jak trzeci
                    if wsp[czwarty][0] != wsp[pierwszy][0] or wsp[czwarty][1] != wsp[trzeci][1]:
                        continue

                if czypustysrodek(pierwszy, drugi, trzeci, czwarty, wsp):
                    return True
