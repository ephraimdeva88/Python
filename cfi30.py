ang1,ang2,ang3=[int(x) for x in(input('Enter the three angles\
 of triangle:')).split(' ')]
print('given angles',ang1,ang2,ang3)
if (180==ang1+ang2+ ang3):
	print('triangle is valid:')
else:
	print('triangle is not valid')