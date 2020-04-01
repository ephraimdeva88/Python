class Employee:
	def set_data(self,n,a,s):
		self._name=n
		self._age=a
		self._salary=s
	def display(self):
		print(self._name,self._age,self._salary)
	def __init__(self,n='',a=0,s=0.0):
		self._name=n
		self._age=a
		self._salary=s
	def __del__(self):
		print('Deleting object'+str(self))
e1=Employee('Ramesh',23,25000)
e1.display()
e2=Employee()
e2.set_data('Suresh',25,30000)
e2.display()
