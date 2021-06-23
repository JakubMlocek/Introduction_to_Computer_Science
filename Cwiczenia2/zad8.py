def fib(x):
    a = 1
    b = 1
    for i in range(x):
        a, b = b, a + b
    return a

def czysumafib(liczba):
    a = 1
    b = 1
    sum = 0
    while sum < liczba:
        sum += a
        a, b = b, a + b

    if sum == liczba:
        return True

    a = 1
    b = 1
    while sum > liczba:
        sum -= a
        a,b = b, a + b

    if sum == liczba:
        return True

n = int(input("Liczba:  "))

while True:
    if(czysumafib(n)):
        print(n)
        break
    n += 1
