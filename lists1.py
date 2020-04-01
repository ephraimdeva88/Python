oddn=[1,3,5,7,9]
print('odd numbers=',oddn)
even=[2,4,6,8,10]
print('even numbers=',even)
c=[*oddn,*even]
print('combination of odd & even numbers:',c)
c=c+[11,17,29]
print('adding prime numbers=',c)
num=len(c)

print('toal elements=',num)
c[10:13]=100,200,300
print('print last 3 replacing elements',c)
c[:]=[]
print(c)
del(c)
