N = int(input('N = '))
a = int(input('a = '))
i = 1
if a==1:
    while i<=N:
        if i%2==1:
            print(i, end=' ')
        i=i+1
elif a==2:
    while i<=N:
        if i%2==0:
            print(i, end=' ')
        i+=1
else:
    print('입력 오류')
