def silnia(n):
    if n < 2:
        return 1
    else:
        return n*silnia(n-1)


def szereg(x, n):
    return ((-1) ** n) * (x ** (2 * n)) / silnia(2 * n)

