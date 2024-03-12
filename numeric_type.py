#int,float,complex

#int
x=1;
x=-10;
print(type(x))
x=123123123123123121;

#float
x=5.3
x=-5.3
print(type(x))

x=35e2#35*10^2
print(x)
print(type(x))

#complex
x=5+3j
print(x)
print(type(x))

#Type conversion
x=5
y=complex(x)
print(y)
print(type(y))

#random
import random#import random module
print(random.randrange(1,10))

#casting
#integer casting
x=int(1)
print(x)
x=int(2.56)
print(x)
x=int("3")
print(x)

#float casting
x=float(3)
print(x)
x=float("3")
print(x)

#str casting
x=('1')
print(type(x))
y=str(1)
print(type(y))

#multiline string
a='''hello,i am there,
This is anshad
from kozhikode'''
print(a)
