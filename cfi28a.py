yr=int(input('enter the leap year:'))
if((yr%4==0) and (yr%100!=0) or (yr%400==0)):
	print('leap year:',yr)
else:
	print('not leap year:',yr)