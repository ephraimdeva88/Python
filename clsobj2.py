#find diff attributes
#find diff objects
#find diff pointing objects
class Complex():
	def __init__(self,r=0.0,i=0.0):
		self._real=r
		self._imag=i
	def __eq__(self,other):
		if self._real==other.__real and self._imag==other.__imag:
			return True
		else:
			return False
c1=Complex(1.0,2.0)
c2=Complex(2.0,3.0)
c3=c1
if c1==c2:
	print('attributes of c1 and c2 are same')
else:
	print('attributes of c1 and c2 are different')
if type(c1)==type(c3):
	print('objects of c1 and c3 are same type')
else:
	print('objects of c1 and c3 are different type')
if c1 is c3:
	print('c1 and c3 are pointing to same object')
else:
	print('c1 and c3 are pointing to different')
