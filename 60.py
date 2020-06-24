def makeList(x):
    return x.split(' ')

fin = open('input.txt')
line = fin.readline()
print(makeList(line))
