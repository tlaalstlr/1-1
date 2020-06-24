#6번째 과제 문제 1번
def perfect(n):
    i,s=1,0
    while i<=n/2:
        if n%i== 0:
            s=s+i
        else:
            pass
        i=i+1
    if n==s:
        return 1
    else:
        if n>s:
            return 3
        else:
            return 2


a = int(input('자연수 a 입력 : '))
while True:
    if perfect(a)==1:
        print('완전수')
    else:
        if perfect(a)==2:
            print('과잉수')
        else:
            print('부족수')
    print()
    a = int(input('자연수 a 입력 : '))
    
