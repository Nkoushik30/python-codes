s1={1,2,3,4,5,6,7}
s2={9,8,6,5,3,7}
print(s1)
print(s2)
print("union:",s1|s2)
print("intersection:",s1&s2)
print("difference:",s1-s2)
print("symmetric diff:",s1^s2)
print(1 in s1)
print(5 in s2)
s1.add('python')
print(s1)
s2.clear()
print("cleared:",s2)
s1.discard('python')
print("discarded:",s1)
s2.add('java')
print(s2)
s2.remove('java')
print(s2)
s1.pop()
print(s1)
s3=s1.copy()
print("s3=",s3)
s2.add(15)
s2.add(18)
s2.add(15)
s2.add(31)
s2.add(5)
s2.add(3)
print("s1=",s1)
print('s2=',s2)
print("difference(s1 and s2):",s1.difference(s2))
print("symmetric diff(s1 and s2):",s1.symmetric_difference(s2))
print("intersection(s1 and s2):",s1.intersection(s2))
print("union(s1 and s2):",s1.union(s2))
