#기말 3
def stringSearch(t, p, i):
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
    
def emailSearch(t, p):
    a = []
    while True:
        l = stringSearch(t, p)
        i = l + M
        if i < N:
            a.append(i)
        else:
            break
    for j in range(len(a)):
        k = a[i]
        x = ""
        while k < N and t[k] != :
            x += t[k]
            k += 1
        a[i] = x
    return a

f = open('email.txt', 'r')
text = f.read()
pattern = "mailto"
result = emailSearch(text, pattern)
for o in range(len(result)):
    print(result[o])
