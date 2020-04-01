#flatten list of list
arr=[[1,2,3,4],[5,6,7,8]]
b=[n for ele in arr for n in ele]#one way
print(b)
c=[*arr[0],*arr[1]]
print(c)