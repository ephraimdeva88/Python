#simple and multiplelie strings
msg1='Honda'
print(msg1)
#escape sequence
msg2='He said,\'Let Us Python\'.'
print(msg2)
file1='c:\\temp\\newfile'
print(file1)
#raw string - prepend r
file2=r'c:\temp\newfile'
print(file2)
#multiline strings
#whitespace at begining of second line becomes part of string
msg3='White is this life if full of care.....\
		We have no time to stand and stare'

#enter at the end of first line becomes part of string
msg4="""What is this life if full of care....
		We have no time to stand and stare"""
#strings are concatenated properly. ()necessary
msg5=('What is this life if full of care ....'
		'We have no time to stand and stare')
print(msg3)
print(msg4)
print(msg5)
#string replication during printing
msg6='MacLearn!!'
print(msg1*3)

#immutability of strings
#Utopia cannot change, msg7 can 
msg7='Utopia'
msg8='Today!!!'
msg7=msg7+msg8 #concatenation using+
print(msg7)

#built-in string function
print(len(msg7))