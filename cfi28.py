#leap year
yr=int(input('Enter the year:'))
if (yr%400==0):
	print('leap year:',yr)
elif(yr%100==0):
	print(' not leap year:',yr)
elif(yr%4==0):
	print(' leap year:',yr)
else:
	print('not leap year:',yr)
