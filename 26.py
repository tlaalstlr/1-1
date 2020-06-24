def isPefect(m):
    a,S=1,0
    while a<=m/2:
        if m%a==0:
            S=S+a
        a=a+1
    if m==S:
        return True

N = int(input('N = '))
for i in range(1, N+1):
    if isPefect(i):
        print(i, end=' ')
