#Jakub Młocek

#program przechodzi kolejno przez Tablice wybierając 3 kolejne niepowtarzające się liczby
#nastepnie sprawdzana jest przerwa miedzy nimi oraz warunek NWD
#jesli te warunki sa spełnione zmienna counter zliczajaca takie mozliwe 3 zwieksza sie o jeden
def NWD(a,b):
    if b == 0:
        return a
    else:
        return NWD(b,a%b)

def trojki(T):
    counter = 0
    N = len(T)
    for pierwsza in range(N):
        for druga in range(pierwsza + 1, N):
            for trzecia in range(druga + 1, N):
                if abs(pierwsza - druga) <= 2 and abs(druga - trzecia) <= 2:
                    #if NWD(NWD(T[pierwsza],T[druga]),T[trzecia]) == 1:
                    if NWD(T[pierwsza],T[druga]) == NWD(T[druga],T[trzecia]) == NWD(T[pierwsza],T[trzecia]) == 1:
                        #print(str(T[pierwsza])+" " +str(T[druga])+" "+str(T[trzecia]))
                        counter += 1
    return counter

print(trojki([2,4,6,7,8,10,12])) # 0 trójek
print(trojki([2,3,4,6,7,8,10])) # 1 trójka (3,4,7)
print(trojki([2,4,3,6,5])) # 2 trójki (2,3,5),(4,3,5)
print(trojki([2,3,4,5,6,8,7])) # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)