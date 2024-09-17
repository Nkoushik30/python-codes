def rfibo(n):
	if n<=1:
		return n
	else:
		return (rfibo(n-1)+rfibo(n-2))
a=int(input("Enter the value of a:"))
if a<=0:
	print("invalid")
else:
	for i in range(a):
		print(rfibo(i))
########################################################
def rfact(n):
	if n==0:
		return 1
	else:
		return n*rfact(n-1)
a=int(input("Enter the value of a:"))
if a<=0:
	print("invalid")
else:
	print("factorial:",rfact(a))
########################################################
x=10
def fun():
	x=20
	print("X:",x)
fun()
print("X:",x)
########################################################
def fun(key):
	if key in dict1:
		print("Key found")
	else:
		print("key not found")
dict1={'name':'shankar','age':19,'section':'d'}
a=input("Enter the key to find:")
fun(a)
#################################################### ##
def rgcd(a,b):
	while(b!=0):
		a,b=b,a%b
	return a
c=int(input("Enter the values to find the GCD:"))
d=int(input())
print("greatest common divisor:",rgcd(c,d))	
#############################################################
