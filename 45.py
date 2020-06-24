# 과제 8-1
N = int(input('N = '))
a = list(range(N+1))
b = 1
c = 1
while b <= N:
    j = c
    while j <= b:
        print(a[j], end=' ')
        j += 1
    print()
    c = b + 1
    b = 2*b + 1
j = c
while j <= N:
    print(a[j], end=' ')
    j += 1
