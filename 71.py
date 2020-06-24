#과제 11-2
def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()

def multiplyMatrix(x, y):
    for i in range(L):
        for j in range(N):
            print(x[i][0]*y[0][j]+x[i][1]*y[1][j], end=' ')
        print()

L = int(input('L = '))
M = int(input('M = '))
N = int(input('N = '))
import random
a = []
for i in range(0, L):
    c = []
    for j in range(0, M):
        c.append(random.randint(-3,3))
    a.append(c)
b = []
for i in range(0, M):
    c = []
    for j in range(0, N):
        c.append(random.randint(-3,3))
    b.append(c)
print('행렬 A')
printMatrix(a)
print()
print('행렬 B')
printMatrix(b)
print()
print('A * B')
multiplyMatrix(a, b)
