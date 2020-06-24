#모의고사 1번문
def isPerfect(x):
    s = 0
    for i in range(1, int(x/2)+1):
        if x % i == 0:
            s += i
    if s == x:
        return 2
    elif s > x:
        return 1
    else:
        return 3

def sumPerfect(a):
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(len(a)):
        if isPerfect(a[i]) == 1:
            s2 += a[i]
        elif isPerfect(a[i]) == 2:
            s1 += a[i]
        else:
            s3 += a[i]
    print('완전수의 합 : ', s1)
    print('과잉수의 합 : ', s2)
    print('부족수의 합 : ', s3)


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
sumPerfect(a)
