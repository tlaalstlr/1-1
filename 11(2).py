a = int(input('a = '))
if a>0:
    print(a, '의 모든 약수 : ', end='')
    i = 1
    while i<= a:
        if a%i==0:
            print(i, end=' ')
        i+=1
else:
    print(a, '는 자연수가 아닙니다.')
