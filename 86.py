#기말 4
def isExpression(s):
    for i in range(len(s)):
        if not (isNumber(s[i]) or s[i] == '+' or s[i] == '-'):
            return False
    return True

def isNumber(s):
    if ord(s) >= 48 and ord(s) <= 57:
        return True
    else:
        return False

def makeInt(s):
    k, n = 0, 0
    for k in range(len(s)):
        n *= 10
        n += ord(s[k]) - 48
    return n
    
def evalList(a):
    while len(a) > 1:
        if a[1] == '+':
            res = a[0] + a[2]
        elif a[1] == '-':
            res = a[0] - a[2]
        a.pop(0)
        a.pop(0)
        a.pop(0)
        a.insert(0, res)
    return a[0]

def makeNumbers(s):
    a = []
    b = ""
    for i in range(len(s)):
        if isNumber(s[i]):
            b += s[i]
        else:
            a.append(makeInt(b))
            b = ""
            a.append(s[i])
    if len(b) != 0:
        a.append(makeInt(b))
    return a


S = input('S = ')
while isExpression(S) != True:
    print('숫자와 +, - 기호만 입력 가능합니다.')
    S = input('S = ')
res = makeNumbers(S)
print('수식 리스트 : ', res)
print('계산 결과 : ', evalList(res))
