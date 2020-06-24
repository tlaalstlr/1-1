def makeNum(x):
    s = 0
    for i in range(len(x)):
        k = ord(x[i]) - 48
        s = s*10
        s += k
    return s

a = input('a = ')
b = input('b = ')
c = makeNum(a)
d = makeNum(b)
e = c + d
print(e)
