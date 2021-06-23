def row_sums(T):
    sums = []
    for row in T:
        sums.append(sum(row))
    return sums

def col_sums(T):
    sums = []
    for col in range(len(T)):
        col_sum = 0
        for row in range(len(T)):
            col_sum += T[row][col]
        sums.append(col_sum)
    return sums



def select_pieces(T,W):
    sum_of_row = row_sums(T)
    sum_of_col = col_sums(T)
    #poszukujemy wiezy szachujacych niezaleznie pola o najwiekszej sumie
    max_sum1 = 0
    max_sum2 = 0
    to_delete1 = None
    to_delete2 = None
    #przechodzimy po wszystkich wiezach
    for i in range(len(W)):
        current_sum = 0
        #sprawdzamy czy jako jedyna w wierszu
        W_cpy = W[:]
        W_cpy.remove(W[i])
        if W[i] not in W_cpy:
            current_sum += sum_of_row[W[i]]
        current_sum += sum_of_col[i]
        #odejmujemy pozycje wiezy od szachowanych pol
        current_sum -= T[W[i]][i]
        if current_sum > max_sum1:
            max_sum2 = max_sum1
            max_sum1 = current_sum
            to_delete2 = to_delete1
            to_delete1 = i
        elif current_sum > max_sum2:
            max_sum2 = current_sum
            to_delete2 = i

    return [to_delete1,to_delete2]



W = [3,4,2,8,7,2,4,2,1]

T = [[1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],]




print(select_pieces(T,W))