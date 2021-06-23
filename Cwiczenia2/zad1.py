def fib(x):
    a = 1
    b = 1
    for i in range(x):
        a, b = b, a + b
    return a

def isCase(liczba):
    for i in range(liczba):
        for j in range(liczba):
            if fib(i) * fib(j) == liczba:
                return True
    return False


liczba = int(input("Podaj Liczbe:  "))

print(isCase(liczba))


 

