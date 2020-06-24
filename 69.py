def longestSequence(num):
    s = set(num)
    print(s)
    max_len = 1
    n = len(num)
    for i in range(n):
        left = num[i]-1
        right = num[i]+1
        count = 1
        while left in s:
            count += 1
            s.discard(left)
            left -= 1
        while right in s:
            count += 1
            s.discard(right)
            right += 1
        max_len = max(max_len, count)
    return max_len

import random
n = int(input('난수의 개수 입력 : '))
numbers = []
for i in range(n):
    x = random.randint(1, n)
    numbers.append(x)
print('리스트 : ', numbers)
max_len = longestSequence(numbers)
print('최장 연속 순차의 길이 : ', max_len)
