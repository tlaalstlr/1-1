# 과제 8-2
def evalTerm(a, x, e):
    t = a
    i = 1
    while i <= e:
        t = t*x
        i += 1
    return t


a = int(input('a = '))
x = int(input('x = '))
e = int(input('e = '))
print('계산 결과 :',evalTerm(a, x, e))
