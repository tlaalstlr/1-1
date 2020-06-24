def stringSearch(t, p):
    i, j = 0, 0
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

fin = open('input.txt', 'r')
text = fin.read()
pattern = input('패턴 입력: ')
N = len(text)
k = stringSearch(text, pattern)
if k < N:
    print('패턴을 처음 발견한 위치:', k)
else:
    print('패턴을 발견하지 못함')
