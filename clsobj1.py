class Fruit():
	count=0
	def __init__(self,name='',size=0,color=''):
		self._name=name
		self._size=size
		self._color=color
		Fruit.count+=1
	def display():
		print(Fruit.count)
f1=Fruit('Banana',5,'yellow')
f2=Fruit('grape',2,'green')
f3=Fruit('apple',10,'red')
Fruit.display()
print(Fruit.count)