def sum_row(t, y):
    return sum(t[y])

def sum_col(t, y):
    return sum(row[x] for row in t)

def place_piecies(board):
    N = len(board)
    row_sums = [sum_row(board ,row) for row in range(N)]
    col_sums = [sum_col(board ,col) for col in range(N)]
    max_sum = 0
    best_p1 = (None , None)
    best_p2 = (None , None)
    #wyplaszczamy tablice
    for i1 in range(N * N - 1):
        for i2 in range(i1 + 1, N*N):
        #powracamy do x -> i y w dol
        y1 = i1 // N
        x1 = i1 % N
        y2, x2 = divmod(i2, N) #to co wyzej szybciej

        s = col_sums[x1] + row_sums[y1] + col_sums[x2] + row_sums[y2]
        #usuwamy gdy wieze nie szachuja nic wzajemnie
        if x1 != x2 and y1 != y2:
            s -= board[y1][x2] + board[y2][x1] + board[y1][x1] + board[y2][x2]

        if y1 == y2 and x1 != x2: #nachodzi na siebie ten sam szachowany wiersz
            s -= row_sums[y1] + board[y1][x1] + board[y2][x2]

        if y1 != y2 and x1 == x2: #nachodzi na siebie ta sama kolumna:
            s -= col_sums[x] + board[y1][x1] + board[y2][x2]

        s -= board[y1][x1] + board[y2][x2] #odejmujemy pola z wiezami

        #print(f"{y1} {x1} {y2} {x2} {s}") #test

        if s > max_sum:
            max_sum = s
            best_p1 = (x1, y1)
            best_p2 = (x2, y2)

    return best_p1, best_p2