area = 64
a = 1
b = area / a**2

mscpoprzec = 6
eps = float(0.1**mscpoprzec)
while abs(a - b) >= eps:
    a = (a + b) / 2
    b = area / a**2

print(str(round(a,mscpoprzec)))