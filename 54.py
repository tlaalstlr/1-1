# 모의고사 3
def isPrime(a):
    i = 2
    while i <= a/2:
        if a % i == 0:
            return False
        i += 1
    return True

def printPrime(a):
    b = 0
    c = 0
    j = 0
    while j < len(a):
        if isPrime(a[j]):
            b += a[j]
        else:
            c += a[j]
        j += 1
    print('소수의 합 :', b)
    print('비소수의 합 :', c)
    

a = []
N = int(input('정수 입력(종료시는 999) : '))
while N != 999:
    if N >= 2:
        if a.count(N)==0:
            a.append(N)
    else:
        print('2 이상의 수만 입력하세요.')
    N = int(input('정수 입력(종료시는 999) : '))
print('생성된 리스트 :', a)
printPrime(a)
