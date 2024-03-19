# class A:
#     def find_sum(self,a,b,c=0,d=0):
#         print(a+b+c+d)
# obj=A()
# obj.find_sum(1,2,3)

class A:
    def find_sum(self,a,b,c=None):
        if(c==None):
            print(a+b)
        else:
            print(a+b+c)

obj=A()
obj.find_sum(1,2,4)