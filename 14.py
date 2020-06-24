a = int(input('a = '))
b = int(input('b = '))
if a>b:
    pass
else:
    a,b=b,a
while not a%b==0:
    f = a%b
    a=f
    a,b=b,a
gcd=b
print(gcd)
