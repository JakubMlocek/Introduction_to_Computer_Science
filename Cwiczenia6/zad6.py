#nie uwzglednia najmniejszej liczebnosci zbioru
wyniki = {}
def najmnpodzbior(T, obecnyel = 0, sumael = 0, sumaindex = 0, ileel = 0):
    global wyniki
    if sumael == sumaindex and sumaindex > 0:
        wyniki[ileel] = sumael
    if obecnyel == len(T):
        return False
    else:
        najmnpodzbior(T,obecnyel + 1, sumael + T[obecnyel], sumaindex + obecnyel, ileel + 1)
        najmnpodzbior(T,obecnyel + 1, sumael, sumaindex, ileel)


T = [1,7,3,5,11,2]
najmnpodzbior(T)
print(wyniki)
mini = min(wyniki.keys())
print(wyniki[mini])