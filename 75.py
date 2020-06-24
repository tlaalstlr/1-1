#6월 10일 모의고사 1
def sumPrime(a):
    i = 0
    n_sum = 0
    p_sum = 0
    for i in range(len(a)):
        if isPrime(a[i]) == True:
            n_sum = n_sum + a[i]
        else:
            p_sum = p_sum + a[i]
    print('소수의 합 : ', n_sum)
    print('비소수의 합 : ', p_sum)

def isPrime(N):
    isPrime = True
    i = 2
    while isPrime == True and i <= N/2:
        if N % i == 0:
            isPrime = False
        i += 1
    return isPrime

x = int(input('정수 입력(종료시는 999) : '))
a = []
while x != 999:
    if x < 2:
        print('2 이상의 수만 입력하세요.')
    else:
        if a.count(x) == 0:
            a.append(x)
    x = int(input('정수 입력(종료시는 999) : '))
print('생성된 리스트 : ', a)
sumPrime(a)
