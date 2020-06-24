import time
N = int(input('자연수N입력 : '))
s = 0
start = time.time()
for i in range(1, N*N+1):
    s+=i
end = time.time() - start
print('합계 :', s)
print('실행시간 :', end)
