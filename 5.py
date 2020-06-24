a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a>b:
    a,b=b,a
else:
    pass
if b>c:
    b,c=c,b
else:
    pass
if a>b:
    a,b=b,a
else:
    pass
print(a ,b ,c)
