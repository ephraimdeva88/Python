#list of collection which is ordered and changeable. Allows duplicate members
#Lets create a list
thislist=["apple","banana","orange"]
print(thislist)
#Access items
#You accesss to the list items by referring to the index number
#print second item of the list

print(thislist[1])
#Change item value
#To change the specific item, refer to the index number
#change to the second item:
thislist[1]="balckberry"
print(thislist)
#Loop through a list
#print all items in the list , one by one
thislist=["apple","banana","orange"]
for x in thislist:
	print(x)
#Check if items Exists
#To determine if a specified item is present in a list use in the keyword
#Check if apple is present in the list
if "apple" in thislist:
	print("yes, 'apple' is in the fruit list")
#List Length
print(len(thislist))
#Add items to the end of the list use append() method
thislist=["apple","banana","cherry"]
thislist.append("orange")
print(thislist)
#To add an item at the specified index
#insert an item as the second position
thislist.insert(1,"grapes")
print(thislist)
#remove an item from the list
thislist.remove("banana")
print(thislist)
#remove last item in the list
thislist.pop()
print(thislist)
#del keyword removes specified index
del thislist[0]
print(thislist)
#del keyword also delete complete list
thislist=["apple","banana","cherry"]

#del thislist
#print(thislist)

#remove all items but not list
thislist.clear()
print(thislist)