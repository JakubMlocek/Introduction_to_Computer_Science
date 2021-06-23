def podzial_l_na_skladniki(liczba, poprz = 1, wszystkie = []):
    if liczba == 0:
        print(wszystkie)
    else:
        for i in range(poprz, liczba+1):
            podzial_l_na_skladniki(liczba - i,i,wszystkie + [i])

podzial_l_na_skladniki(4)