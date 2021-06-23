#Jakub Młocek

def maxi(T):
    #szukamy wiersza z najwieksza liczba
    N = len(T)
    pierwsza1zlewej = N
    najwwiersz = N
    for i in range(N):
        for j in range(N):
            if T[i][j] == 1:
                if j < pierwsza1zlewej:
                    pierwsza1zlewej = j
                    najwwiersz = i
                elif j == pierwsza1zlewej: #sprawdzamy gdy taka sama liczba jedynek
                        for k in range(j,N): #sprawdzamy kolejne jedynki
                            if T[i][k] == 1 and T[najwwiersz][k] != 1:
                                najwwiersz = i
                                break
    return najwwiersz

def mini(T):
    #szukamy wiersza z najmniejsza lcizba
    N = len(T)
    pierwsza1zprawej = 0
    najmwiersz = 0
    i = j = N-1
    while i >= 0:
        while j >= 0:
            if T[i][j] == 1:
                if j > pierwsza1zprawej:
                    pierwsza1zprawej = j
                    najmwiersz = i
                elif j == pierwsza1zprawej: #sprawdzamy gdy taka sama liczba jedynek
                        k = j
                        while k >= 0: #sprawdzamy kolejne jedynki
                            if T[i][k] != 1 and T[najmwiersz][k] == 1:
                                najmwiersz = i
                                break
                            k -= 1
        j -= 1
    i -= 1
    return najmwiersz




def distance(T):
    maxwiersz = maxi(T)
    minwiersz = mini(T)
    return (abs(minwiersz-maxwiersz)) #odleglosc miedzy wierszami rozumiem jako modol roznicy ich pozycji

    #szukamy najwiekszej binarnej (najwiecej jedynek z przodu)

