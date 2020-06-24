#리스트 회전
def rotate(nums, k, n):
    if k > n:
        k %= n
    res = list(range(1, n+1))
    for i in range(k):
        res[i] = nums[n-k+i]
    j = 0
    for i in range(k, n):
        res[i] = nums[j]
        j += 1
    return res

N = int(input('원소의 개수: '))
k = int(input('회전 단계수: '))

numbers = list(range(1, N+1))
print('원래 리스트 : ', numbers)
result = []
result = rotate(numbers, k, N)
print('회전 리스트: ', result)
