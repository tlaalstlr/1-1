#주사위 n번 던진 후 확률
def castDice(N):
    i = 1
    a = []
    while i <= N:
        import random
        a.append(random.randint(1,6))
        i = i + 1
    j = 1
    while j <= 6:
        print(j, a.count(j)/N*100,'%')
        j = j + 1

N = int(input('N = '))
castDice(N)
