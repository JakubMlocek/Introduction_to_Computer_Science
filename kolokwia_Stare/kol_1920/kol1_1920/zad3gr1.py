
def ruch(T, N, w, k, s):
    if w == N - 1:
        return s == 0
    else:
        for nk in range(N):
            if abs(nk - k) >= 2:
                if ruch(T, N, w + 1, nk, s + T[w + 1][nk]):
                    return True
        return False

def krol(T, N):
    for k in range(N):
        if ruch(T, N, 0, k, T[0][k]):
            return True
    return False


