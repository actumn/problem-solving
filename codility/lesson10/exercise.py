def divisors(n):
    i = 1
    result = 0
    while i * i < n:
        if n % i == 0:
            result += 2
        i += 1
    if i * i == n:
        result += 1
    return result

def primality(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True