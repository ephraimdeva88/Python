x1,y1,x2,y2,x3,y3=[int(x)for x in input('enter three points:')\
.split(',')]
a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) 
if (a == 0): 
	print ("Yes")
else: 
	print("No")