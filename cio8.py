data=input('Enter Name of\
	the person ,\
	years of service,\
	Diwali bonus received:').split(',')
name=data[0]
y=float(data[1])
db=float(data[2])
ded=2*y+db*5.5/100
print(ded)