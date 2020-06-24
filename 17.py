a = int(input('a = '))
i = 1
s = 0
while i<=a/2:
    if a % i == 0:
        s = s + i
    else:
        pass
    i = i + 1
if a == s:
    print(a ,'은(는) 완전수 입니다.')
else:
    print(a ,'은(는) 완전수가 아닙니다.')
