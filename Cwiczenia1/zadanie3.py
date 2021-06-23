suma = 1
a1 = 0
a2 = 0
b1 = 1
b2 = 1

czyjest = False
szukana = 21

while(b2 <= szukana):
    if suma == szukana:
        czyjest = True
        break
    elif suma < szukana:
        a2, b2  = b2, a2 + b2
        suma += b2
    elif suma > szukana:
        suma -= a1
        a1, a2 = b1, a1 + b1

if czyjest:
    print("Tak")
else:
    print("Nie")
