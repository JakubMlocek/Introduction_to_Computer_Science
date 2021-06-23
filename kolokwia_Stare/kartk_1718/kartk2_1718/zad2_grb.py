def czydwarownoliczne(T, pierwszy = [], drugi = []):
    if len(pierwszy) == len(drugi) and sum(pierwszy) == sum(drugi) and pierwszy and drugi:
        return True
    if not T:
        return False
    else:
        pierwszy_cpy = pierwszy[:]
        drugi_cpy = drugi[:]
        return czydwarownoliczne(T[1:], pierwszy_cpy + [T[0]], drugi_cpy) or \
                czydwarownoliczne(T[1:], pierwszy_cpy, drugi_cpy + [T[0]]) or \
                czydwarownoliczne(T[1:], pierwszy_cpy, drugi_cpy)

T = [1,2,10]

print(czydwarownoliczne(T))





