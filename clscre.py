class Employee():
	def set_data(self,n,a,s):
		self._name=n
		self._age=a
		self._salary=s
	def get_data(self):
		print(self._name,self._age,self._salary)
e1=Employee()
e1.set_data('ephraim',25,1000000)
e1.get_data()
