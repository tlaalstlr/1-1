def encipher(p, k):
    a = ord(p)
    if a == 32: a = 64
    t = a + k
    if a < 91:
        if t >= 91: t += 6
    if t > 122: t -= 59
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
