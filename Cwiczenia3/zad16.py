def czyjedennaj(tab):
    tab = sorted(tab)
    if tab[0] != tab[1] and tab[-1] != tab[-2]:
        return True
    else:
        return False

def pojedyncze_min_max(tab):
    only_min = True
    only_max = True
    min = max = tab[0]

    for i in range(1,len(tab)):
        if tab[i] == max:
            only_max = False
        elif tab[i] > max:
            max = tab[i]
            only_max = True

        if tab[i] == min:
            only_min = False
        elif tab[i] < min:
            min = tab[i]
            only_max = True
    return only_max and only_min

tab = [1,2,3,5,33,21,4,5,2,7,8,55]
print(pojedyncze_min_max(tab))