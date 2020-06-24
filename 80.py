def sumFour(a):
    i = 0
    b = []
    while i < len(a):
        s1 = a[i] + a[i+2]
        s2 = a[i+1] + a[i+3]
        b.append(s1)
        b.append(s2)
        i += 4
    while b.count(0) != 0:
        b.remove(0)
    print('B = ', b)

N = int(input('N = '))
a = []
import random
for j in range(N):
    a.append(random.randint(1, 3))
print('A = ', a)
while len(a) % 4 != 0:
    a.append(0)
sumFour(a)
