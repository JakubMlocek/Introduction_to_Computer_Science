N = int(input("N:   "))

N -= 1 #bedziemy szukac do liczby N-1
sito = [True for _ in range(N)]
sito[0] = False
sito[1] = False
print(sito)

i = 2
while i * i <= N:
    if sito[i] == True:
        j = i * i
        while j <= N - 1:
            sito[j] = False
            j = j + i
    i += 1

print(sito)
for i in range(len(sito)):
    if sito[i]:
        print(i)