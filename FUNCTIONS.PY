def add(a,b):
	print ('adition',a+b)
def sub(a,b):
	print ('subtraction',a-b)
def mul(a,b):
	print ('multiplication',a*b)
def div(a,b):
	print ('division',a/b)
a=int (input("Enter  the a value: "))
b=int(input("Enter the value of b: "))
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)
######################################################
def num(a,b):
	while b:
		a,b=b,a%b
	return a	
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(num(a,b))
#########################################################33
def A(a):
	if  a>0:
		return '+ve'
	elif a<0:
		return '-ve'
	else:
		return 'NULL'	
a=int(input("Enter the value of a:"))
print(A(a))
##########################################
def small(l):
	return min(l),max(l)
l=[1,32,45,6,3,56,2,64]
print(small(l))
print("minimum number is :",min(l))
print("maximum number  is :",max(l))
###########################################
def add(l):
	f=[]
	for i in l:
		for j in i:
			f.append(j)
	return f
l=[[1,2,4,5,3,5,3,4],[31,25,6,67,86,78]]
print(add(l))
#######################################
def small(l):
	l.remove(max(l))
	print('second maximum of list:',max(l))
l=[1,32,45,6,3,56,2,64]
small(l)
