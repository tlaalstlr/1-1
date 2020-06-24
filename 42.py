def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def preprocessing(s):
    i = 0
    j = 0
    l = len(s)
    t = ''
    while i < l:
        if s[i].isalpha():
            t += s[i]
            i += 1
        else:
            i += 1
    t = t.lower()
    return t

s = input('문자열 입력:')
s = preprocessing(s)
print('변환된 문자열:', s)
if isPalindrome(s):
    print('회문입니다.')
else:
    print('회문이 아닙니다.')
