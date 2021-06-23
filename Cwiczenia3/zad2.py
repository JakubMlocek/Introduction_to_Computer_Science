def czytesamecyfry(pierwsza, druga):
    pierwsza = sorted(pierwsza)
    druga = sorted(druga)
    #print(pierwsza)
    #print(druga)
    return pierwsza == druga

def czytesamecyfryv2(pierwsza, druga):
    wielokrotnosccyfr = [0 for _ in range(10)]
    wielokrotnosccyfrdruga = [0 for _ in range(10)]
    while pierwsza > 0:
        wielokrotnosccyfr[pierwsza%10] += 1
        pierwsza //= 10
    # mozna tez odejmowac od pierwszej tablicy i sprawdzic czy kazdy element ma 0
    while druga > 0:
        wielokrotnosccyfrpierwsza[pierwsza%10] += 1
        pierwsza //= 10
    return wielokrotnosccyfrpierwsza == wielokrotnosccyfrdruga

pierwsza = input("Podaj liczbe 1:  ")
druga = input("Podaj liczbe 2:  ")
print(czytesamecyfry(pierwsza,druga))


