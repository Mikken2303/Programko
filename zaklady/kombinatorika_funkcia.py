def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

def komb(n,k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

print(komb(8,2))