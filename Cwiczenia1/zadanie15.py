wyraz = 0.5**0.5
iloczyn = 1

dokladnosc = 6

for i in range(dokladnosc):
    iloczyn *= wyraz
    wyraz = (0.5 + 0.5*wyraz)**0.5

    print(iloczyn)

pi = float(2/iloczyn)

print(round(pi,dokladnosc))
