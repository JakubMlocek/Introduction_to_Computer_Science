
N = 4
#T1 = [ [0] * N for i in range(N) ]
T1 = [[1,2,3,4],[14,17,19,89],[8,14,18,22],[3,4,14,20]]
T2 = [0] * N**2

pozycjaT2 = 0
removed = []
for p in range(N**2):
    minwwierszu = 0
    min = 9999999999
    for wiersz in range(N):
        try:
            if T1[wiersz][0] < min:
                minwwierszu = wiersz
                min = T1[wiersz][0]
        except:
            continue
    if min not in T2 and min not in removed:
        T2[pozycjaT2] = min
        pozycjaT2 += 1
    elif min in removed:
        pass
    else:
        T2.remove(min)
        removed.append(min)
        pozycjaT2 -= 1
    T1[minwwierszu] = T1[minwwierszu][1:]



print(T1)
print(T2)