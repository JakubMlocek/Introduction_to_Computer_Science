def nwd(a, b):
    while(b):
        a, b = b, a % b
    return a

a = 12
b = 16
c = 26

print(nwd(a,nwd(b,c)))
