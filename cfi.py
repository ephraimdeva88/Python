#age=15
#statu='minor' if age<18 else 'adult' #sets minor
#problem 4.1
#While purchasing certain items,a discount of 10% is offered if the quatity purchased is more than
#1000. If quantity and price per item are input through the keyboard, write a progra to calculate
#thee total expenses
qty=int(input('Enter value of quatity:'))
price=float(input('Enter value of price:'))
if qty>1000:
	dis=10
else:
	dis=0
totexp=qty*price-qty*price*dis/100
print('Total expenses =Rs.'+str(totexp))