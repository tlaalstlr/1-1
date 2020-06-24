#과제 10-1
def everySearch(t, p):
    while True:
        l = stringSearch(t, p)
        i = l + M
        if i < N:
            print('패턴을 발견한 위치:', l)
        else:
            break

def stringSearch(t, p):
    global i
    j = 0
    N = len(t)
    M = len(p)
    while i < N and j < M:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M:
        return i - M
    else:
        return i

text = 'A lover asked his beloved, Do you love yourself more than you love me?'
print('텍스트 :', text)
pattern = input('패턴 입력 : ')
i = 0
N = len(text)
M = len(pattern)
everySearch(text,pattern)
print('문자열 탐색 완료.')

