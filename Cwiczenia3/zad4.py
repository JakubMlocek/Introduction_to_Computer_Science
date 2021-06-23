def silnia(liczba):
    if liczba == 0 or liczba == 1:
        return 1
    else:
        return liczba * silnia(liczba - 1)

def obliczE(eps):
    rozwiniecie = [0 for _ in range(eps)]
    for i in range(100): #dokladnosc e w wyliczaniu
        obecnasilnia = silnia(i)
        element = int(1/obecnasilnia)
        bufor = 1 % obecnasilnia
        rozwiniecie[0] += element
        if bufor == 0:
            continue
        for c in range(1, eps):
            bufor *= 10
            rozwiniecie[c] += (int(bufor/obecnasilnia))
            #print(bufor)
            #print(rozwiniecie[c])
            bufor %= obecnasilnia
        c = eps - 1
        while c > 0:
            if rozwiniecie[c] >= 10:
                rozwiniecie[c] %= 10
                rozwiniecie[c - 1] += 1
            c -= 1
    return rozwiniecie

print(obliczE(100))
e = 0
for i in range(100):
 e += 1/silnia(i)
print(e)