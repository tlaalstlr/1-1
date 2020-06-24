def countMinMax(a, d):
    b = []
    a.sort()
    i = MIN
    while i < MAX:
        b.append(a.index(i+1)-a.index(i))
        i += 1
    b.append(len(a)-a.index(MAX)+1)
    return b

N = int(input('N = '))
MIN = int(input('MIN = '))
MAX = int(input('MAX = '))
A = []
import random
for j in range(N):
    A.append(random.randint(MIN, MAX))
D = MAX - MIN
res = countMinMax(A, D)
print()
print('난수      빈도수      비율 ')
print('===========================')
for k in range(D+1):
    print('%d        %d          %.1f%%'%(MIN+k, res[k], res[k]*100/N))
