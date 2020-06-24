# 영문 소문자로 이루어진 문자열을 입력 받아 암호문으로 변환하는 프로그램 작성
def encipher(p):
    a = ord(p)
    if a == 32:
        a = 96
    t = a + k
    if t > 122:
        t -= 27
    if t == 96:
        t = 32
    return chr(t)

p = input('평문 입력 : ')
k = int(input('K 값 입력(1~26) : '))
while k < 1 or k > 26:
    k = int(input('K 값 입력(1~26) : '))
n = len(p)
c = ''
for i in range(n):
    ch = encipher(p[i])
    c += ch
print('암호문 출력 : [', end='')
print(c, end='')
print(']')
