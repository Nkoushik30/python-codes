s=input("Enter the string:").split()
for i in s:
	if len(i)%2==0:
		print(i)
#############################
s=input("Enter the string :")
c=0
print(len(s))
for i in s:
	c+=1
print('length=',c)
#########################
s= input("Enter the string:")
c,v=0,0
for i in s:
	if i in "aeiouAEIOU":
		v+=1
	else:
		c+=1
print("vowels=",v)
print("consonants=",c)
##################################
d={1:346,'a':34,'b':34}
print(d)
d.update({2:20})
print(d)
print("noof keys=",d.keys())
print("dict values=",d.values())
print(d.get('a'))
d1=d.copy()
print('d1=',d1)
######################
s=input("Enter the string :")
rev=''
for i in s:
	rev=i+rev
print(rev)
#####################
s=input("Enter the string:")
rev=''
for i in s:
	rev=i+rev
if rev==s:
	print('palindrome')
else:
	print("not a palindrome")
