x,y=[float(z)for z in input('enter x and y values:')\
.split(',')]
if (x==0 and y==0):
	print('point lies on the origin')
elif(x==0):
	print('point lies on y axis')
elif(y==0):
	print('point lies on x axis')