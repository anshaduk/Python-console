# # # # # class A:
# # # # #     def __init__(self,name,place,age):
# # # # #         self.name=name
# # # # #         self._place=place
# # # # #         self.__age=age
# # # # #     def method(self):
# # # # #         print(self.__age)
# # # # #         print(self._place)
# # # # # a=A('anshad','calicut',10)

# # # # # print(a._place)
# # # # # a.method()

# # # # #Recursion
# # # # # def recursive(n):
# # # # #     if n==1:
# # # # #         return 1
# # # # #     else:
# # # # #         return n*recursive(n-1)
    
# # # # # res=recursive(5)
# # # # # print(res)

# # # # #arbitary argument
# # # # # def my_fun(*kids):
# # # # #     print("The youngest is "+kids[1])

# # # # # my_fun('a','b','c')

# # # # #keyvalue
# # # # # def my_fun(child3,child2,child1):
# # # # #     print('the youngest child is:',child3)

# # # # # my_fun(child1='a',child2='b',child3='c')

# # # # #lambda
# # # # # res=lambda a,b:a+b
# # # # # print(
# # # # #     res(2,3))

# # # # # high_order=lambda x,fun:x+fun(x)
# # # # # high_order(20,lambda x:x*x)

# # # # # even=lambda x:(x%2 and 'odd' or 'even')
# # # # # print(even(4))

# # # # #Decorator
# # # # # def dec(func):
# # # # #     def inner():
# # # # #         res=func()
# # # # #         return res.upper()
# # # # #     return inner

# # # # # @dec
# # # # # def greeting():
# # # # #     return "hello"

# # # # # print(greeting())


# # # # # def dunc():
# # # # #     print("python")

# # # # # a=dunc
# # # # # a()

# # # # # print(dir(dunc))

# # # # # def call_fun(x,func):
# # # # #     print(func(x))

# # # # # def double(n):
# # # # #     return n*2

# # # # # call_fun(2,double)

# # # # # def gen():
# # # # #     yield 10
# # # # #     yield 20
# # # # #     yield 30


# # # # # x=gen()
# # # # # print(next(x))
# # # # # print(next(x))

# # # # # def gen():
# # # # #     for i in range(10):
# # # # #         yield(i)
    
# # # # # y=gen()
# # # # # # print(next(y))
# # # # # # print(next(y))
# # # # # # print(next(y))

# # # # # for i in y:
# # # # #     print(i)

# # # # # res=[x**2 for x in range(10)]
# # # # # print(res)

# # # # # fruits=['a','b','c','d']
# # # # # itr_obj=iter(fruits)
# # # # # print(next(itr_obj))
# # # # # print(next(itr_obj))
# # # # # print(next(itr_obj))

# # # # # a=1
# # # # # b=0
# # # # # try:
# # # # #     if b==0:
# # # # #         raise Exception("exception raised1")
# # # # #     c=a/b
# # # # #     print(c)
# # # # # except Exception as e:
# # # # #     print('exception raised')
# # # # # else:
# # # # #     print('no exception')
# # # # # finally:
# # # # #     print("ends..")

# # # # # class invalidData(Exception):
# # # # #     pass
# # # # #     marks=int(input())
# # # # #     try:
# # # # #          if marks<0 and marks>100:
# # # # #               raise invalidData
# # # # #     except invalidData:
# # # # #          print("hello")

# # # # class motor:
# # # #     def __init__(self):
# # # #         self.name='motor'
# # # #         self.brand='hello'
# # # #     def display(self):
# # # #         print(f"name is {self.name} and brand is {self.brand}")
# # # # class bmw(motor):
# # # #     def __init__(self):
# # # #         super().__init__()
# # # #         self.color='red'
    
# # # #     def dis_data(self):
# # # #         print(f"{self.name} {self.color}")
# # # # m=motor()
# # # # m.display()
# # # # b=bmw()
# # # # b.dis_data()

# # # # class product:
# # # #     def __init__(self,name,price):
# # # #         self.name=name
# # # #         self.price=price
    
# # # #     def __add__(self,other):
# # # #         print("add operator called")

# # # # p1=product('a',1)
# # # # p2=product('b',2)
# # # # p1+p2
        
# # # # class A:
# # # #     def func(self):
# # # #         print("func called from parent")
    
# # # # class B(A):
# # # #     def func(self):
# # # #         print("func called from B")
# # # #         super().func()

# # # # b1=B()
# # # # b1.func()

# # # class Animal:
# # #     def perform(self):
# # #         print("animal perform in the circus")
# # # class Human:
# # #     def perform(self):
# # #         print("human perform in circus")
# # # class Circus:
# # #     def play(self,animal:Animal):
# # #         animal.perform()

# # # tiger=Animal()
# # # abc=Human()
# # # c=Circus()
# # # c.play(abc)

# # # from abc import ABC,abstractmethod
# # # class vehicle(ABC):
# # #     def startengine(self):
# # #         print("start engine")
# # #     def applybreak(self):
# # #         print('apply break')
# # #     @abstractmethod
# # #     def applygear(self):
# # #         pass
# # # class car(vehicle):
# # #     def applygear(self):
# # #         print('change gear manually')

# # class Enc:
# #     __a=10
# #     def __display(self):
# #         print("welcome")
# #         print(self.__a)
# #     # def new(self):
# #     #     self.__display()
# # b=Enc()
# # b._Enc__display()    
# # # b.new()    

# class myClass:
#     def __init__(self,value):
#         self._value=value
#     @property
#     def pytvalue(self):
#         return self._value
    
#     @pytvalue.setter
#     def pytvalue(self,new_value):
#         self._value=new_value

# obj=myClass(45)
# obj.pytvalue=100
# print(obj.pytvalue)

# res=list(map(int,input().split()))
# print(res)
# res1=list(filter(lambda n:n%2==0,res))
# print(res1)
# from functools import reduce
# res2=reduce(lambda a,b:a+b,res1)
# print(res2)
    
