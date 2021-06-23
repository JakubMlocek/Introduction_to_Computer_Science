def nwd(a, b):
    while(b):
        a, b = b, a % b
    return a

def nww(a,b):
    return a*b/nwd(a,b)

a = 12
b = 16
c = 24

print(nww(nww(a,b),c))