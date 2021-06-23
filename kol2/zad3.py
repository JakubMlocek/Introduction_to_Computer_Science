#Jakub Młocek

#rozwiazanie polega na rozpłaszczeniu tablicy a nastepnie dla kazdej mozliwej
#pozycji wiez sprawdzenie sumy szachowanej przez nie pól

def sum_row(t, y):
    return sum(t[y])

def sum_col(t, x):
    return sum(row[x] for row in t)

def chess(board):
    N = len(board)
    row_sums = [sum_row(board ,row) for row in range(N)]
    col_sums = [sum_col(board ,col) for col in range(N)]
    max_sum = None
    best = (None,None,None,None)
    #wyplaszczamy tablice
    for i1 in range(N * N - 1):
        for i2 in range(i1 + 1, N*N):
        #powracamy do x -> i y w dol
            y1, x1 = divmod(i1, N)
            y2, x2 = divmod(i2, N)

        s = col_sums[x1] + row_sums[y1] + col_sums[x2] + row_sums[y2]
        s -= 2*(board[y1][x1] + board[y2][x2])

        if x1 != x2 and y1 != y2: #usuwamy gdy wieze nie szachuja nic wzajemnie
            s -= (board[y1][x2] + board[y2][x1])

        elif y1 == y2 and x1 != x2: #nachodzi na siebie ten sam szachowany wiersz
            s -= (row_sums[y1] )

        elif y1 != y2 and x1 == x2: #nachodzi na siebie ta sama kolumna:
            s -= (col_sums[x1])


        if max_sum == None:
            max_sum = s
            best = (y1, x1, y2, x2)
        elif s > max_sum:
            max_sum = s
            best = (y1, x1, y2, x2)

    return best, max_sum

print(chess([[4,0,2],[3,0,0],[6,5,3]])) # (0,1,1,0) suma=17
print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]]))  # (2,3,3,1) suma=35