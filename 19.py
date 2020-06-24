def power(x,y):
    res = x
    for i in range(y-1):
        res *=x
    return res

a = int(input('a = '))
b = int(input('b = '))
result = power(a,b)
print(result)
