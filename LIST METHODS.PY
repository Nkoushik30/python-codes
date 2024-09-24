l1=["M","na","i","Abhi"]
l2=["y","me","s","Ram"]
l3=[i+j for i,j in zip(l1,l2)]
print(l3)
#############
l=[]
n=int(input("Enter the value of n:"))
for i in range(n):
	ele=int(input("Enter the values of list:"))
	l.append(ele)
print(l)
print(max(l))
print(min(l))
#############
l=[]
n=int(input("Enter the value of n:"))
for i in range(n):
	ele=int(input("Enter the values of list:"))
	l.append(ele)
print(l)
l2=[]
l3=[]
for i in range(n):
	if(l[i]%2==0):
		l2.append(l[i])
	else:
		l3.append(l[i])
print(l2)
print(l3)
###############
l=[]
n=int(input("Enter the value of n:"))
for i in range(n):
	ele=int(input("Enter the values of list:"))
	l.append(ele)
print(l)
if len(l)>0:
	l[0],l[-1]=l[-1],l[0]
print(l)
#####################
l=[]
sum=0
n=int(input("Enter the value of n:"))
for i in range(n):
	ele=int(input("Enter the values:"))
	sum+=ele
	l.append(ele)
print(l)
print(sum)
print(sum/n)
