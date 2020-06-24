def isPrime(a):
    i=2
    while i <= a/2:
        if a % i == 0:
            return False
        else:
            i = i + 1
    return True

N = int(input('N = '))
if isPrime(N):
    print(a, end=' ')
