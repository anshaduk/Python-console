#id()
str="hello"
print(id("hello"))
print(id(str))

#is checking  the id of object pointed by x is same as the id of object pointed by y
x=5
y=5
print(id(x))
print(id(y))
print(x is y)#id of x pointed object is same as the id of y pointed object.

#is not  the id of object pointed by x is not same as the id of object pointed by y
x="abc"
y="xyz"
print(x is not y)
