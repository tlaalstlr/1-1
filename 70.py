#과제 11-1
def twoSumSorted(num, t):
    n = len(num)
    for i in range(n):
        for j in range(i+1, n):
            if num[i] + num[j] == t:
                print('%d 번째와 %d 번째 원소'%(i+1, j+1))

import random
n = int(input('리스트의 원소 개수 입력 : '))
numbers = []
for i in range(n):
    numbers.append(random.randint(1, n*2))
numbers.sort()
print('정렬된 리스트 : ', numbers)
x = set(numbers)
numbers = list(x)
print('중복이 제거된 리스트 : ', numbers)
target = int(input('목표값 입력 : '))
print('두 수의 합이 %d인 원소 쌍'%target)
twoSumSorted(numbers, target)
