def f(x):
    return 1/x

def pole(pocz, koniec, eps):
    odcinek = float((koniec - pocz) / eps)
    sum = 0.0
    srodek = pocz + odcinek/2
    for i in range(eps):
        sum += (f(srodek) * odcinek)
        srodek += odcinek
    return sum


pocz = 1
koniec = int(input("Podaj koniec:  "))
eps = 20
print(pole(pocz, koniec, eps))
