def result_of_function(number):
    return number ** number - 2020


def bisekcja(p ,k , eps):
    while k - p > eps:
        s = (p + k) / 2
        if result_of_function(p) * result_of_function(k) < 0:
            k = s
        else:
            p = s
    return s

def bisekcja_cw(p, k, eps):
    #while True:
    while k - p > eps:
        s = (p + k) / 2
        if result_of_function(s) < 0:
            p = s
        else:
            k = s
        #if abs(result_of_function(s)) < eps:
        #    return s
    return s


print(str(bisekcja(1, 10, 1e-7)))
print(str(bisekcja_cw(1, 10, 1e-7)))

# 1e-10