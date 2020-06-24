def printPoly(p):
    print(p)
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
    print("다항식 = ", res)

def evalPoly(p, x):
    sum = 0
    res = ""
    res += ("%dx^%d "%(p[0][1], p[0][0]))
    a = 1
    for j in range(p[0][0]):
        a *= x
    a *= p[0][1]
    sum += a
    for i in range(1, len(p)):
        b = 1
        if p[i][0] > 1:
            if p[i][1] > 0:
                res += ("+ %dx^%d "%(p[i][1], p[i][0]))
            elif p[i][1] < 0:
                res += ("- %dx^%d "%(abs(p[i][1]), p[i][0]))
            else:
                pass
            for k in range(p[i][0]):
                b *= x
            b *= p[i][1]
            sum += b
        elif p[i][0] == 1:
            if p[i][1] > 0:
                res += ("+ %dx "%(p[i][1]))
            elif p[i][1] < 0:
                res += ("- %dx "%(abs(p[i][1])))
            else:
                pass
            b *= p[i][1]
            b *= x
            sum += b
        else:
            if p[i][1] > 0:
                res += ("+ %d "%(p[i][1]))
            elif p[i][1] < 0:
                res += ("- %d "%(abs(p[i][1])))
            else:
                pass
            sum += p[i][1]
            
    print("다항식 = ", res)
    print("X = ", x)
    print("계산 결과 : ", sum)

def addPoly(A, B):
    res_A = ""
    res_A += ("%dx^%d "%(A[0][1], A[0][0]))
    for i in range(1, len(A)):
        if A[i][0] > 1:
            if A[i][1] > 0:
                res_A += ("+ %dx^%d "%(A[i][1], A[i][0]))
            elif A[i][1] < 0:
                res_A += ("- %dx^%d "%(abs(A[i][1]), A[i][0]))
            else:
                pass
        elif A[i][0] == 1:
            if A[i][1] > 0:
                res_A += ("+ %dx "%(A[i][1]))
            elif A[i][1] < 0:
                res_A += ("- %dx "%(abs(A[i][1])))
            else:
                pass
        else:
            if A[i][1] > 0:
                res_A += ("+ %d "%(A[i][1]))
            elif A[i][1] < 0:
                res_A += ("- %d "%(abs(A[i][1])))
            else:
                pass
    print("다항식  A = ", res_A)
    res_B = ""
    res_B += ("%dx^%d "%(B[0][1], B[0][0]))
    for j in range(1, len(B)):
        if B[j][0] > 1:
            if B[j][1] > 0:
                res_B += ("+ %dx^%d "%(B[j][1], B[j][0]))
            elif B[j][1] < 0:
                res_B += ("- %dx^%d "%(abs(B[j][1]), B[j][0]))
            else:
                pass
        elif B[j][0] == 1:
            if B[j][1] > 0:
                res_B += ("+ %dx "%(B[j][1]))
            elif B[j][1] < 0:
                res_B += ("- %dx "%(abs(B[j][1])))
            else:
                pass
        else:
            if B[j][1] > 0:
                res_B += ("+ %d "%(B[j][1]))
            elif B[j][1] < 0:
                res_B += ("- %d "%(abs(B[j][1])))
            else:
                pass
    print("다항식  B = ", res_B)
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
    res_C = ""
    res_C += ("%dx^%d "%(C[0][1], C[0][0]))
    for j in range(1, len(C)):
        if C[j][0] > 1:
            if C[j][1] > 0:
                res_C += ("+ %dx^%d "%(C[j][1], C[j][0]))
            elif C[j][1] < 0:
                res_C += ("- %dx^%d "%(abs(C[j][1]), C[j][0]))
            else:
                pass
        elif C[j][0] == 1:
            if C[j][1] > 0:
                res_C += ("+ %dx "%(C[j][1]))
            elif C[j][1] < 0:
                res_C += ("- %dx "%(abs(C[j][1])))
            else:
                pass
        else:
            if C[j][1] > 0:
                res_C += ("+ %d "%(C[j][1]))
            elif C[j][1] < 0:
                res_C += ("- %d "%(abs(C[j][1])))
            else:
                pass
    print("A + B = ", res_C)

def multiplyPoly(A, B):
    res_A = ""
    res_A += ("%dx^%d "%(A[0][1], A[0][0]))
    for i in range(1, len(A)):
        if A[i][0] > 1:
            if A[i][1] > 0:
                res_A += ("+ %dx^%d "%(A[i][1], A[i][0]))
            elif A[i][1] < 0:
                res_A += ("- %dx^%d "%(abs(A[i][1]), A[i][0]))
            else:
                pass
        elif A[i][0] == 1:
            if A[i][1] > 0:
                res_A += ("+ %dx "%(A[i][1]))
            elif A[i][1] < 0:
                res_A += ("- %dx "%(abs(A[i][1])))
            else:
                pass
        else:
            if A[i][1] > 0:
                res_A += ("+ %d "%(A[i][1]))
            elif A[i][1] < 0:
                res_A += ("- %d "%(abs(A[i][1])))
            else:
                pass
    print("다항식  A = ", res_A)
    res_B = ""
    res_B += ("%dx^%d "%(B[0][1], B[0][0]))
    for j in range(1, len(B)):
        if B[j][0] > 1:
            if B[j][1] > 0:
                res_B += ("+ %dx^%d "%(B[j][1], B[j][0]))
            elif B[j][1] < 0:
                res_B += ("- %dx^%d "%(abs(B[j][1]), B[j][0]))
            else:
                pass
        elif B[j][0] == 1:
            if B[j][1] > 0:
                res_B += ("+ %dx "%(B[j][1]))
            elif B[j][1] < 0:
                res_B += ("- %dx "%(abs(B[j][1])))
            else:
                pass
        else:
            if B[j][1] > 0:
                res_B += ("+ %d "%(B[j][1]))
            elif B[j][1] < 0:
                res_B += ("- %d "%(abs(B[j][1])))
            else:
                pass
    print("다항식  B = ", res_B)
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
    res_C = ""
    res_C += ("%dx^%d "%(C[0][1], C[0][0]))
    for j in range(1, len(C)):
        if C[j][0] > 1:
            if C[j][1] > 0:
                res_C += ("+ %dx^%d "%(C[j][1], C[j][0]))
            elif C[j][1] < 0:
                res_C += ("- %dx^%d "%(abs(C[j][1]), C[j][0]))
            else:
                pass
        elif C[j][0] == 1:
            if C[j][1] > 0:
                res_C += ("+ %dx "%(C[j][1]))
            elif C[j][1] < 0:
                res_C += ("- %dx "%(abs(C[j][1])))
            else:
                pass
        else:
            if C[j][1] > 0:
                res_C += ("+ %d "%(C[j][1]))
            elif C[j][1] < 0:
                res_C += ("- %d "%(abs(C[j][1])))
            else:
                pass
    print("A * B = ", res_C)

    

p = [[5, 3], [3, 5], [1, 4], [0, 2]]
A = [[5, 3], [3, 5], [1, 4], [0, 2]]
B = [[5, 2], [2, 4], [1, 3]]
#printPoly(p)
x = 2
#evalPoly(p, x)
#addPoly(A, B)
multiplyPoly(A, B)
