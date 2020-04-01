#fname,mname,lname=input('enter your name:').split()
#print('firstname:',fname,'middlename:',mname,'lastname:',lname)
#n1,n2,n3=[int(n) for n in input('Enter three values:').split()]
#print(n1+10,n2+20,n3+30)
#numbers=[int(x) for x in input('Enter values:').split()]
#for n in numbers:
#	print(n+1)
data=input('Enter name,age,salary:').split(',')
name=(data[0])
age=int(data[1])
salary=float(data[2])
print(name,age,salary)