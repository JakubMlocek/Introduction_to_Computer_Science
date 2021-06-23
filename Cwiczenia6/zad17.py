def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n < 2:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

uniqe = {}

def del_el(liczba, pozycja):
    tmp_num = ""
    for i in range(len(liczba)):
        if i != pozycja:
            tmp_num += liczba[i]
    return tmp_num


def create(liczba, nowa = ""):
    if liczba == "":
        if is_prime(int(nowa)):
            uniqe[nowa] = True
    else:
        for i in range(len(liczba)):
            create(del_el(liczba,i) , nowa + liczba[i])



create("123"+"75")
for key, value in uniqe.items():
    print(key)
