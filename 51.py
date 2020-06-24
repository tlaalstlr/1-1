# n*m 행렬 속은 난수로
n = int(input('n = '))
m = int(input('m = '))

def inputMatrix(n, m):
    import random
    A = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(random.randint(0, 3))
        A.append(b)
    return A

def printMatrix(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j], end=' ')
        print()

printMatrix(inputMatrix(n, m))
