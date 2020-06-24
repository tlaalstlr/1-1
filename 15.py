while True:
    a = int(input('a = '))
    b = int(input('b = '))
    A = a
    B = b
    while A != B:
        if A > B:
            B = B + b
        else:
            A = A + a
    print(A)
