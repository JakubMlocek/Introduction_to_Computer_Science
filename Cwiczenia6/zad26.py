
zbudowane = {}
def zbuduj(A, B, obecna = "1"):
    if A == 1 and B == 0:
        zbudowane[obecna] = True
    else:
        if A - 1 >= 1:
            zbuduj(A-1,B,obecna+"1")
        if B - 1 >= 0:
            zbuduj(A,B-1,obecna+"0")


zbuduj(2,3)
for key in zbudowane.keys():
    print(key)

