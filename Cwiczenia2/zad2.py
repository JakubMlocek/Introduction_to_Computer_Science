def wersjazstringiem(a,b,n):
    wynik = str(a//b) + "."
    bufor = a % b
    for i in range(n):
        bufor *= 10
        wynik += str(int(bufor / b))
        bufor %= b
    print(wynik)

def wesjabezstringa(a,b,n):
    print(a//b, end=".")
    bufor = a % b
    for i in range(n):
        bufor *= 10
        print(int(bufor / b), end = "")
        bufor %= b


a = int(input("a:  "))
b = int(input("b:  "))
n = int(input("n:  "))

wesjabezstringa(a,b,n)
#wersjazstringiem(a,b,n)


