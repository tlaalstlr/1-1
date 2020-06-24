a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > b:
    a,b=b,a
else:
    pass
if b > c:
    b,c=c,b
else:
    pass
D = c
while D%a !=0 or D%b != 0:
    D = D + c
print(D)
