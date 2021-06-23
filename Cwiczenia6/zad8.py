def czymozliwawaga(odwazniki, szukana, obecnyodwaznik):
    if szukana == 0:
        return True
    if obecnyodwaznik == len(odwazniki):
        return False
    return czymozliwawaga(odwazniki, szukana - odwazniki[obecnyodwaznik], obecnyodwaznik + 1)\
           or czymozliwawaga(odwazniki, szukana + odwazniki[obecnyodwaznik], obecnyodwaznik + 1) \
           or czymozliwawaga(odwazniki, szukana, obecnyodwaznik + 1)


odwazniki = [1,3,5,9]
print(czymozliwawaga(odwazniki,7, 0))
