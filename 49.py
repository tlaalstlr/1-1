#버블 정렬
def bubblesort(a, n):
    for i in range(n, 1, -1):
       for j in range(1, i):
           if a[j] > a[j+1]:
               a[j], a[j+1] = a[j+1], a[j]
    return a

import random, time
N = 5
a = []
a.append(-1)
for i in range(1, N+1):
    a.append(random.randint(1,N))
start_time = time.time()
b = bubblesort(a, N)
end_time = time.time() - start_time
print(end_time)

print(b)
