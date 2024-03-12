x=5;#integer
print(type(x))

x=1.5#float
print(type(x))

x=1j;#complex
print(type(x))

x=['apple','banana','cherry']#list
print(type(x))

x=('apple','banana','cherry')#tuple
print(x)
print(type(x))

x=range(6)#range
print(x)
print(type(x));

x={'name':'anshad','age':29}#dict
print(x)
print(type(x))

x={"apple","banana","cherry"}#set
print(type(x))

x=frozenset({"banana",'cherry',"grapes"})#frozenset
print(type(x))

x=True;#bool
print(type(x))

x=b"hello"#bytes
print(x)
print(type(x))

x=bytearray(5)#bytearray
print(x)
print(type(x))

x=memoryview(bytes(5))#memoryview
print(x)
print(type(x))

x=None#NoneType
print(x)
print(type(x))

#specify data type
x=str("hello")
print(type(x))

x=bool(5)
print(x)

x=dict(name='ram',age=25)
print(x)
