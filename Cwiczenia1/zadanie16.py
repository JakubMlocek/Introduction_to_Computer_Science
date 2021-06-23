maxlkrok = 0
maxA0 = 2
for i in range(2,10001):
    previous = i
    lkrok = 1
    next = (previous % 2) * (3 * previous + 1) + (1 - previous % 2) * previous / 2
    while(next != 1):
        lkrok += 1
        next = (previous % 2) * (3 * previous + 1) + (1 - previous % 2) * previous / 2
        previous = next

    if lkrok > maxlkrok:
        maxlkrok = lkrok
        maxA0 = i

print(maxA0)


