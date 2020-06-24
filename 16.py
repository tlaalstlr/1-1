a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
A = a
B = b
C = c
while A != B:
    if A > B:
        B = B + b
    else:
        A = A + a
    while A != C:
        if A > C:
            C = C + c
        else:
            A = A + a
print(C)
