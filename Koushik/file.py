f=open('demo.txt','r')
print(f.read())
f.close()
f=open('demo.txt','w')
f.write('welcome to python week 8\n')
f.close()
f=open('demo.txt','a')
f.write(" Hello World.\n")
f.close()
f=open('demo.txt','r')
print("read line: ",f.readline())
f.close()
f=open('demo.txt','r')
print('noof bytes to read: ',f.read(15))
f.close()
f=open('demo.txt','r+')
f.write("cse\n")  # it will append the first three letters of the ('welcome to python week 8')  this line
f.close()
f=open('demo.txt','r')
print("reading lines: ",f.readlines())
f.close()
f=open('demo.txt','w')
lines=[
   "first line of the program file.\n","second line of the program file.\n","third line of the program file.\n"
   ]
print(f.writelines(lines))
f.close()
f=open('demo.txt','r')
pos=f.tell()
print("position of the cursur: ",pos)
f.seek(10)
print("position of the cursur after seek method: ",f.tell())
