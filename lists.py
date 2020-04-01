names=['Anil','Amol','Aditya','Avi','Alka']
print('disply the list=',names)
names.insert(3,'Anuj')
print("insert a name 'Anuj' before 'Aditya'",names)
names.append('Zulu')
print("Append a name 'Zulu'",names)
del(names[4])
print("delete Avi'names",names)
names[0]='Anilkumar'
print(names)
names.sort()
print(names)
names.reverse()
print(names)
