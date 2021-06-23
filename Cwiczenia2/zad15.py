from math import pow

def sumaNtychpotcyfr(liczba,N):
    l = liczba
    sum = 0
    while liczba > 0:
        sum += int(pow(liczba % 10, N))
        liczba //= 10
        #print(sum)
        #print(liczba)
    return sum == l



N = int(input("Ponaj N:  "))

scope = pow(10,N)

#print(sumaNtychpotcyfr(153,3))

for liczba in range(int(scope)):
    if sumaNtychpotcyfr(liczba,N):
        print(liczba)