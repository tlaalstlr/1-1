# 6번째 과제 문제 2
A = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]
B = [[4, 5, 6], [4, 3, 2], [2, 1, 3]]
def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()

def addMatrix(m,n):
    for i in range(len(m)):
        for j in range(len(m[i])):
                print(m[i][j]+n[i][j], end=' ')
        print()

print('행렬 A')
printMatrix(A)
print()
print('행렬 B')
printMatrix(B)
print()
print('A + B')
addMatrix(A,B)
