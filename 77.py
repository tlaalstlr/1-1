#6월 10일 모의고사 3
def makeMatrix(m):
    import random
    a = []
    for i in range(m):
        b = []
        for j in range(m):
            if i == j:
                b.append(0)
            else:
                b.append(random.randint(0, 3))
        a.append(b)
    return a

def printMatrix(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()

def subMatrix(a):
    i = 0
    s1, s2 = 0, 0
    while i < len(a):
        j = 0
        while j < len(a[i]):
            if i < j:
                s1 += a[i][j]
            else:
                s2 += a[i][j]
            j += 1
        i += 1
    return (s1, s2)

M = int(input('M = '))
x = makeMatrix(M)
printMatrix(x)
result = subMatrix(x)
print('결과 : %d - %d = %d' %(result[0], result[1], result[0]-result[1]))
