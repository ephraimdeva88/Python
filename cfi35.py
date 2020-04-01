ang1,ang2,ang3=[int(x)for x in input('enter angles:\
	').split(',')
tt=180			 
if(tt==ang1+ang2+ang3 and tt>ang1+ang2 or tt>ang1+ang3 or \
	tt>ang2+ang3 or tt>ang1+ang3):
	print('valid triangle:')
else:
	print('invalid triangle:')
