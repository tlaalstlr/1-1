def lcm(m,n):
    A,B=a,b
    while A != B:
        if A>B:
            B=B+b
        else:
            A=A+a
    return A

a = int(input('a = '))
b = int(input('b = '))
print('최소공배수 :', lcm(a,b))
