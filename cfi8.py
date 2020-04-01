num=int(input('Enter value of num:'))
i=2
while i<=num-1:
	if num%1==0:
		print('Not a prime number')
		break
	i+=1
else:
	print('Prime number')