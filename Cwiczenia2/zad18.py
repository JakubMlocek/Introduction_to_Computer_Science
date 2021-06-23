def ciagAn(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ciagAn(n-1) - ciagBn(n-1) * ciagAn(n-2)


def ciagBn(n):
    if n == 0:
        return 2
    else:
        return ciagBn(n-1) + 2 * ciagAn(n-1)

i = 0
x = int(input("podaj " + str(i) + " wyraz ciagu an:  "))
while x == ciagAn(i):
    print("wyraz " + str(i) + " ciagu Bn: " + str(ciagBn(i)))
    i += 1
    x = int(input("podaj " + str(i) + " wyraz ciagu an:  "))