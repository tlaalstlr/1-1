N = int(input('N = '))
if N <= 2:
    print('N은 2보다 큰 자연수여야 합니다.')
else:
    pass
a = 6
while a <= N:
    i = 1
    S = 0
    while i <= a/2:
        if a % i == 0:
            S = S + i
        i = i + 1
    if a == S:
        print(a, end=' ')
    a = a + 1
