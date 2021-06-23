def row_sum(T, N, row):
    return sum(T[row])

def kol_sum(T, N, kol):
    return sum(row[kol] for row in T )

def sum_of_chess(x1,y1,x2,y2):
    s = col_sums[x1] + row_sums[y1] + col_sums[x2] + row_sums[y2]
    # usuwamy gdy wieze nie szachuja nic wzajemnie
    if x1 != x2 and y1 != y2:
        s -= board[y1][x2] + board[y2][x1] + board[y1][x1] + board[y2][x2]

    if y1 == y2 and x1 != x2:  # nachodzi na siebie ten sam szachowany wiersz
        s -= row_sums[y1] + board[y1][x1] + board[y2][x2]

    if y1 != y2 and x1 == x2:  # nachodzi na siebie ta sama kolumna:
        s -= col_sums[x] + board[y1][x1] + board[y2][x2]

    s -= board[y1][x1] + board[y2][x2]  # odejmujemy pola z wiezami
    return s

def app(T, N, x1, y1, x2, y2):
    given_sum = sum_of_chess(x1,y1,x2,y2)
    for il in range(N*N):
        y, x = divmod(il,N)
            actual_sum1 = sum_of_chess(x,y,x1,y1)
            actual_sum2 = sum_of_chess(x,y,x2,y2)
            if actual_sum1 > given_sum or actual_sum2 > given_sum:
                return True
    return False
