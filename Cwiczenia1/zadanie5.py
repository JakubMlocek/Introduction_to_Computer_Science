area = 13
a = 1
b = area / a

mscpoprzec = 6
eps = float(0.1**mscpoprzec)
while abs(a - b) >= eps:
    a = (a + b) / 2
    b = area / a

print(str(round(a,mscpoprzec)))