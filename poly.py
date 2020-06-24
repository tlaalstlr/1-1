def inputPoly():
    P = []
    q = int(input('지수 : '))
    c = int(input('계수 : '))
    while q >= 0:
        if len(P) == 0:
            l = []
            l.append(q)
            l.append(c)
            P.append(l)
        else:
            k = 0
            for i in range(len(P)):
                if P[i][0] == q:
                    k += 1
            if k >= 1:
                print('같은 지수 값을 가지는 원소가 있습니다.')
            else:
                l = []
                l.append(q)
                l.append(c)
                P.append(l)
        q = int(input('지수 : '))
        c = int(input('계수 : '))
    P = sorted(P, key = lambda x : -x[0])
    print('다항식 리스트 : ', P)
    return P
    
def printPoly(p):
    res = ""
    res += ("%dx^%d "%(p[0][1], p[0][0]))
    for i in range(1, len(p)):
        if p[i][0] > 1:
            if p[i][1] > 0:
                res += ("+ %dx^%d "%(p[i][1], p[i][0]))
            elif p[i][1] < 0:
                res += ("- %dx^%d "%(abs(p[i][1]), p[i][0]))
            else:
                pass
        elif p[i][0] == 1:
            if p[i][1] > 0:
                res += ("+ %dx "%(p[i][1]))
            elif p[i][1] < 0:
                res += ("- %dx "%(abs(p[i][1])))
            else:
                pass
        else:
            if p[i][1] > 0:
                res += ("+ %d "%(p[i][1]))
            elif p[i][1] < 0:
                res += ("- %d "%(abs(p[i][1])))
            else:
                pass
    print(res)

def evalPoly(p, x):
    f = 0
    a = 1
    for j in range(p[0][0]):
        a *= x
    a *= p[0][1]
    f += a
    for i in range(1, len(p)):
        b = 1
        if p[i][0] > 1:
            for k in range(p[i][0]):
                b *= x
            b *= p[i][1]
            f += b
        elif p[i][0] == 1:
            b *= p[i][1]
            b *= x
            f += b
        else:
            f += p[i][1]
    return f

def addPoly(A, B):
    t = ""
    C = []
    C.extend(A)
    C.extend(B)
    C = sorted(C, key = lambda x : -x[0])
    for k in range(1, len(C)):
        if C[k-1][0] == C[k][0]:
            C[k-1][1] += C[k][1]
            t += str(k)
    for l in range(len(t)-1, -1, -1):
        C.pop(int(t[l]))
    return C

def multiplyPoly(A, B):
    C = []
    t = []
    for k in range(len(A)):
        for l in range(len(B)):
            C.append([A[k][0]+B[l][0], A[k][1]*B[l][1]])
    C = sorted(C, key = lambda x : -x[0])
    for k in range(1, len(C)):
        if C[k-1][0] == C[k][0]:
            C[k-1][1] += C[k][1]
            t.append(k)
    for l in range(len(t)-1, -1, -1):
        C.pop(t[l])
    return C
    
m = 1
while m != 9:
    print('1. 다항식 입력')
    print('2. 다항식 출력')
    print('3. 다항식 계산')
    print('4. 다항식 덧셈')
    print('5. 다항식 곱셈')
    m = int(input('메뉴 선택 (종료시는 9) : '))
    if m == 1:
        print('다항식 입력 선택\n')
        P = inputPoly()
    elif m == 2:
        print('다항식 출력 선택\n')
        printPoly(P)
    elif m == 3:
        print('다항식 계산 선택\n')
        printPoly(P)
        X = int(input('X = '))
        result = evalPoly(P, X)
        print('계산 결과 : ', result)
    elif m == 4:
        print('다항식 덧셈 선택\n')
        A = inputPoly()
        B = inputPoly()
        printPoly(A)
        printPoly(B)
        C = addPoly(A, B)
        printPoly(C)
    elif m == 5:
        print('다항식 곱셈 선택\n')
        A = inputPoly()
        B = inputPoly()
        printPoly(A)
        printPoly(B)
        C = multiplyPoly(A, B)
        printPoly(C)
    else:
        if m != 9:
            print('메뉴 선택 오류\n')
