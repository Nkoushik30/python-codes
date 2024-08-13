def fact(n):
	f=1
	for i in range(1,n+1):
		f*=i
	return f
n=int(input("enter :"))
for i in range(0,n+1):
	print(" "*(n-i),end=" ")
	for j in range(0,i+1):
		print(fact(i)//(fact(i-j)*fact(j)),end=" ")
	print(" ")
