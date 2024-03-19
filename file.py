f1=open('abc.txt','w')
f1.write("welcome to python")
f1.close()

f1=open('abc.txt','r')
print(f1.read(5))
print(f1.read(5))

f1.close()
