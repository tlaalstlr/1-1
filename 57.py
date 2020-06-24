def encipher(p, k):
    a = ord(p)
    if a == 32: a = 64
    t = a + k
    if a < 91:
        if t >= 91: t += 6
    if t > 122: t -= 59
    if t == 64: t = 32
    return chr(t)

def decipher(c, k):
    a = ord(c)
    if a == 32: a = 64
    t = a - k
    if a >= 97:
        if t < 97: t -= 6
    if t < 64 : t += 59
    if t == 64: t = 32
    return chr(t)

k = int(input('K = '))
p = input('평문 : ')
n = len(p)
c = ''
for i in range(n):
    ch = encipher(p[i], k)
    c += ch
print('암호문 : [', end='')
print(c, end='')
print(']')
q = ''
for i in range(n):
    ch = decipher(c[i], k)
    q += ch
print('복호화된 평문 : [', end='')
print(q, end='')
print(']')
