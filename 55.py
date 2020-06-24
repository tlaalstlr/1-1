# 모의고사 4
def printRation(n, minValue, maxValue):
    i = 1
    a = []
    print('난수      빈도수')
    print('================')
    while i <= n:
        import random
        a.append(random.randint(minValue, maxValue))
        i += 1
    a.sort()
    a.append(maxValue+1)
    for j in range(minValue, maxValue+1):
        print(j, a.index(j+1))
        for k in range(a.index(j+1)):
            a.remove(j)
            
N = int(input('N = '))
MIN = int(input('MIN = '))
MAX = int(input('MAX = '))
printRation(N, MIN, MAX)
