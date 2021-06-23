def czymozliwawaga(odwazniki, szukana, obecnyodwaznik, sumazwazonych = 0):
    if szukana == sumazwazonych:
        return True
    if obecnyodwaznik == len(odwazniki):
        return False
    return czymozliwawaga(odwazniki, szukana, obecnyodwaznik + 1, sumazwazonych + odwazniki[obecnyodwaznik]) \
    or czymozliwawaga(odwazniki, szukana, obecnyodwaznik + 1, sumazwazonych)


odwazniki = [1,3,5,9]
print(czymozliwawaga(odwazniki,17, 0))
