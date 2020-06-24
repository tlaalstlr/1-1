#모의고사 2
def makeMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()

def printMatrix(A):
    c = 0
    d = 0
    e = 0
    for i in range(len(A)):
        c += A[i].count(0)
        d += A[i].count(1)
        e += A[i].count(2)
    print('0의 개수 :', c)
    print('1의 개수 :', d)
    print('2의 개수 :', e)


n = int(input('n = '))
import random
b = []
for i in range(0, n):
    a = []
    for j in range(0, n):
        a.append(random.randint(0,2))
    b.append(a)
print()
makeMatrix(b)
print()
printMatrix(b)
