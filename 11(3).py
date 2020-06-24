a = int(input('자연수 입력: '))
while a <= 0:
    print(a, '는 자연수가 아닙니다.')
    a = int(input('자연수 입력: '))
print(a, '의 모든 약수 : ', end='')
i = 1
while i<= a:
    if a%i==0:
        print(i, end=' ')
    i+=1
