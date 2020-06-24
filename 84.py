#기말 2
def makeMatrix(m):
    import random
    a = []
    for i in range(m):
        b = []
        for j in range(m):
            if i == j:
                b.append(0)
            else:
                b.append(random.randint(0, 1))
        a.append(b)
    return a

def printMatrix(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()

def exchangeMatrix(a):
    c1 = 0
    c2 = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i < j:
                if a[i][j] == a[j][i]:
                    c1 += 1
                else:
                    c2 += 1
                    a[i][j], a[j][i] = a[j][i], a[i][j]
    return c1, c2, a


N = int(input('N = '))
x = makeMatrix(N)
printMatrix(x)
print()
result = exchangeMatrix(x)
print('대칭인 원소의 개수 : ', result[0])
print('대칭이 아닌 원소의 개수 : ', result[1])
print()
printMatrix(result[2])
