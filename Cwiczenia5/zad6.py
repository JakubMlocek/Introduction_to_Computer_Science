def dod(z1,z2):
    re = z1[0] + z2[0]
    im = z1[1] + z2[1]
    return (re,im)

def odej(z1,z2):
    re = z1[0] - z2[0]
    im = z1[1] - z2[1]
    return (re,im)

def mn(z1,z2):
    re = z1[0]*z2[0] - z1[1] * z2[1]
    im = z1[0]*z2[1] - z2[0] * z1[1]
    return (re,im)

def dziel(z1, z2):
    if z2[0] != 0 or z2[1] != 0:
        re = (z1[0] * z2[0] + z1[1] * z2[1]) / (z2[0] ** 2 + z2[1] ** 2)
        im = (z2[0] * z1[1] - z1[0] * z2[1]) / (zw[0] ** 2 + z2[1] ** 2)
        return (re, im)
    else:
        print("Przez 0 to sie :)")

def pot(z,l):
