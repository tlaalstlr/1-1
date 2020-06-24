N = int(input('N = '))
import random
a = []
for i in range(N):
    a.append(random.randint(1, N))
s = set(a)
print(s)
b = list(range(1, N+1))
print('집합에 없는 원소 : ', end='')
for j in b:
    if j not in s:
        print(j, end = ' ')
