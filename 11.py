a = int(input('a = '))
if a>0:
	pass
else:
	print('a는 자연수가 아닙니다.')
i = 1
while i<= a:
	if a%i==0:
		print(a, '의 모든 약수 :', i, end='')
	else:
		pass
	i += 1