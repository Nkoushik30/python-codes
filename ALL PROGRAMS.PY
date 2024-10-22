n=int(input("enter the value of n:"))
sum=0
i=0
while i<n:
	i=i+1
	sum=sum+i
print(sum)
###
a=int(input("enter the value of a:"))
i=1
sum=0
while a>0:
	rem=a%10
	sum=sum+rem
	a=a//10
print(sum)
###
m=int(input("enter the value of m:"))
fact=1
for i in range(1,m+1,1):
	fact=fact*i
print(fact)
###
print("tables using for loop")
n=10
k=int(input("enter table name in maths value:"))
i=1
for i in range(1,n+1):
	print(k,"x",i,"=",k*i)
print("tables using while loop")
n=10
k=int(input("enter the table name in maths:"))
i=1
while i<=n:
	print(k,"x",i,"=",k*i)
	i+=1
