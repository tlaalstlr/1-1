fout = open('output.txt', 'w')
for c in range(0, 51, 9):
    f = c*9/5 + 32
    out = '섭씨 온도 : %d, 화씨 온도 : %.1f\n' %(c, f)
    fout.write(out)
fout.close()
