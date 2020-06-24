a = 50000
s = 0
b = 0
c = 50000
d = 0
for i in range(120):
    a *= 1.01
    b += a*0.01
    s += a
    d += c
print('총합 :',s)
print('이득 :',b)
print('그냥 :',d)
for j in range(10):
    s *= 1.01
print('10년 투자후 10년 가만히:', s)
