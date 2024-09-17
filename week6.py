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
