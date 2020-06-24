N = int(input('N = '))
a = int(input('a = '))
if a==1:
    for i in range(1,N):
        if i%2==1:
            print(i, end=' ')
elif a==2:
    for i in range(1,N):
        if i%2==0:
            print(i, end=' ')
else:
    print('입력 오류')
