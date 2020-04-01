Ram,Shyam,Ajay=input('Enter ages of Ram,Shyam and Ajay:')\
	.split(' ')
if (Ram>=Shyam and Ram>=Ajay): 
	print('Youngest boy is Ram:',Ram)
elif(Shyam>=Ram and Shyam>=Ajay ):
	print('Youngest:',Shyam)
elif(Ajay>=Ram and Ajay>=Shyam):
	print('Youngest:',Ajay)