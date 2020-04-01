num=int(input('Enter five digit number:'))
test_num=0
while (num>0):
	remainder=num%10
	test_num=(test_num*10)+remainder
	num=num//10
print('Reverse number is :',test_num)