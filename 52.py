def twoSum(a, n):
    i = 0
    while i < n-1:
        b.append(a[i]+a[i+1])
        i += 2
    if n%2 == 1:
        b.append(a[-1])
    return b

N = int(input('N= '))
import random
a = []
b = []
for i in range(1, N+1):
    a.append(random.randint(1,5))
print(a)
print(twoSum(a, N))
