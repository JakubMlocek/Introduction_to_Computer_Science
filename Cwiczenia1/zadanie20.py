an = 15.0
bn = 23.0

eps = 0.00000001

while abs(an - bn > eps):
    an1 = (an * bn)**0.5
    bn1 - (an + bn)/2.0
    an = an1
    bn = bn1

print(bn)