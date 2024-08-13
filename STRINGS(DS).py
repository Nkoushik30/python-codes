s="hello"
s1="world!"
s3="12343456"
print(s+s1)
print(s*3)
for i in "Hello world":
	print(i)
print('e' in "hello world")
print('r' in "hello")
print("from index 0-unknown:",s[0:])
print("from index 4-unknown:",s[4:])
print("from index 0-3",s[:3])
print("from indexs 1-5:",s[1:5])
print("from index -1:",s[-1:])
print('capitalize=',s.capitalize())
print('upper=',s1.upper())
print(s.isupper())
print(s1.islower())
a="HELLO WORLD"
print(a)
print('lower=',a.lower())
print('title=',a.title())
tx="my name is {fname},I am {age}".format(fname='John doe',age=23)
print(tx)
print("is all num=",s.isalnum())
print("is alpha=",s1.isalpha())
print("is num=",s3.isdigit())
