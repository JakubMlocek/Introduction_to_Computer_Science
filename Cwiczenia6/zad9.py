odwazniki = [1,2,3,5,8,13]
def czymozliwawaga(szukana, obecnyodwaznik = 0, wybraneodwazniki = []):
    if szukana == 0:
        return wybraneodwazniki
    if obecnyodwaznik == len(odwazniki):
        return False
    return czymozliwawaga(szukana - odwazniki[obecnyodwaznik], obecnyodwaznik + 1, wybraneodwazniki + [odwazniki[obecnyodwaznik]])\
           or czymozliwawaga(szukana, obecnyodwaznik + 1, wybraneodwazniki) \
           or czymozliwawaga(szukana + odwazniki[obecnyodwaznik], obecnyodwaznik + 1,wybraneodwazniki + [-odwazniki[obecnyodwaznik]])

print(czymozliwawaga(4))