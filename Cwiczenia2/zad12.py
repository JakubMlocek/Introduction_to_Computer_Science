def isleninnumber(sequence):
    sequencecopy = sequence
    l = 0
    while sequence > 0:
        sequence //= 10
        l += 1
    #print(l)
    sequence = sequencecopy
    while sequence > 0:
        #print(sequence % 10)
        if sequence % 10 == l:
            return True
        sequence //= 10
    return False



liczba = int(input("Liczba:  "))
print(isleninnumber(liczba))