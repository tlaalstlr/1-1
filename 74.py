def binarySearch(nums, key):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if key == nums[mid]:
            return mid
        if key > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

import random
N = int(input('데이터의 개수 입력 : '))
data = 0
numbers = []
for i in range(N):
    data += random.randint(1, 5)
    numbers.append(data)
print('리스트 : ', numbers)
searchKey = int(input('탐색 키 입력 : '))
result = binarySearch(numbers, searchKey)
if result == -1:
    print('탐색 키와 동일한 원소가  없습니다.')
else:
    print('리스트의 %d 번째 원소' %(result+1))
