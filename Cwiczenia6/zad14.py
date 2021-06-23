def hanoi(n, A, B, C):
    if n == 1:
        C.append(A.pop())
        print(A, B, C)
    else:
        hanoi(n-1, A, C, B)
        C.append(A.pop())
        print(A, B, C)
        hanoi(n-1, B, A, C)

number = 3  # w przypadku 3 krazkow
a = ["a"]
b = ["b"]
c = ["c"]
for i in range(number):
    a.append(number-i)
print (a, b, c)
hanoi(number, a, b, c)