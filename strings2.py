s='Bamboozled'
#extra B a
print(s[-10],s[-9],s[-8],s[-7],s[-6],s[-5],s[-4],s[-3],s[-2],s[-1])
print(s[0],s[1])
print(s[-10],s[-8])
#extra e d
print(s[8],s[9])
print(s[-2],s[-1])
#extract mbo ozled
print(s[2:10])
print(s[2:])
print(s[-8])

#extract Bamboo
print(s[0:6])
print(s[:6])
print(s[-10:-4])
print(s[:-4])

print(s[0:10:1])
print(s[0:10:2])
print(s[0:10:3])
print(s[0:10:4])

s=s+'Hype!'
print(s)
s=s[:6]+'Monger'+s[-1]
print(s)  
