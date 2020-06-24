#6월 10일 모의고사 2
def sumThree(a, n):
    i = 0
    b = []
    while i < len(a):
        b.append(a[i]+a[i+1]+a[i+2])
        i += 3
    print('b = ', b)

N = int(input('N = '))
a = []
import random
for j in range(N):
    a.append(random.randint(1, 5))
print('a = ', a)
while len(a) % 3 != 0:
    a.append(0)
sumThree(a, N)
