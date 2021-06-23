def czypierwsza(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False

    i = 5
    while i <= n**0.5:
        if n % i == 0 or n % (i+2):
            return False
        i += 6
    return True

print(czypierwsza(5))


