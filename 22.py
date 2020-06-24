def gcd(m,n):
    i = 1
    while i<=a and i<=b:
        if a%i==0 and b%i==0:
            gcd=i
        i=i+1
    return gcd

a = int(input('a = '))
b = int(input('b = '))
print('최대공약수 :', gcd(a,b))
