def makeNumbers(s):
    a = []
    b = ''
    for i in range(len(s)):
        if isNumber(s[i]) == True:
            b += s[i]
        else:
            a.append(b)
            b = ''
    a.append(b)
    while a.count('') != 0:
        a.remove('')
    print('숫자 리스트 : ', a)


def isAlnum(s):
    for i in range(len(s)):
        if not (s[i].isalnum()):
            return False
    return True

def isNumber(s):
    if ord(s) >= 48 and ord(s) <= 57:
        return True
    else:
        return False

S = input('S = ')
while isAlnum(S) != True:
    print('숫자와 문자만 입력 가능합니다.')
    S = input('S = ')
makeNumbers(S)
