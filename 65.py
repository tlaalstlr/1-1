#과제 10-2
def rotate(a, k):
    for i in range(k):
        for j in range(len(a)-2, -1, -1):
            a[j], a[j+1] = a[j+1], a[j]
            print(a)
    print('회전 리스트 : ', a)
            

N = int(input('원소의 개수: '))
k = int(input('회전 단계수: '))

numbers = list(range(1, N+1))
print('원래 리스트 : ', numbers)
rotate(numbers, k)

