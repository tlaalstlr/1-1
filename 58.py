fin = open('input.txt', 'r')
text = fin.read()
print('텍스트:', text)
fin.close()

fin = open('input.txt')
line = fin.readline()
print(line, end='')

fin = open('input.txt')
for i in range(3):
    line = fin.readline()
    print(line, end='')
    
fin = open('input.txt')
line = fin.readline()
while line:
    print(line, end='')
    line = fin.readline()
