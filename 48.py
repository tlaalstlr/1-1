#암호화된 문자열을 복호화하여 다시 평문으로 변환하는 함수 decipher(c)
def encipher(p):
    a = ord(p)
    if a == 32: a = 96
    t = a + k
    if t > 122: t -= 27
    if t == 96: t = 32
    return chr(t)

def decipher(c):
    a = ord(c)
    if a == 32: a = 96
    t = a - k
    if t < 96: t += 27
    if t == 96: t = 32
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
q = ''
for i in range(n):
    ch = decipher(c[i])
    q += ch
print('복호화된 평문 : [', end='')
print(q, end='')
print(']')
