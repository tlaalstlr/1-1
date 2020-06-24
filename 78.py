#6월 10일 모의고사 4
def makeNumber(s):
    k, n = 0, 0
    for k in range(len(s)):
        n *= 10
        n += ord(s[k]) - 97
    return n

def isAtoj(s):
    for i in range(len(s)):
        t = ord(s[i])
        if t < 97 or t > 106:
            return False
    return True

S1 = input('S1 = ')
while isAtoj(S1) == False:
    print('a 부터 j 사이의 영문 소문자만 입력 가능합니다.')
    S1 = input('S1 = ')
S2 = input('S2 = ')
while isAtoj(S2) == False:
    print('a 부터 j 사이의 영문 소문자만 입력 가능합니다.')
    S2 = input('S2 = ')
s1 = makeNumber(S1)
s2 = makeNumber(S2)
print('%d + %d = %d' %(s1, s2, s1+s2))
