#난수 발생 후 최댓값과 최솟값 구하기
def maxMin(a):
    maxValue = a[0]
    for i in range(1, len(a)):
        if maxValue <= a[i]:
            maxValue = a[i]
        i += 1
    minValue = a[0]
    for j in range(1, len(a)):
        if minValue >= a[j]:
            minValue = a[j]
        j += 1
    return (maxValue, minValue)

N = int(input('N = '))
import random
a = []
for k in range(10):
    a.append(random.randint(1, N))
print(a)
result = maxMin(a)
print('최댓값 = %d, 최솟값 = %d' %(result[0], result[1]))
