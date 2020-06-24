def sum_avg(x,y,z):
    global s,a
    s = x+y+z
    a = s/3

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
sum_avg(a,b,c)
print('s =',s)
print('a =',a)
