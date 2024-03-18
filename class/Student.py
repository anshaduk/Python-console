class Student:
    def __init__(self,name,id,physics,chemistry,maths):
        self.name=name
        self.id=id
        self.physics=physics
        self.chemistry=chemistry
        self.maths=maths
    
    def total_marks(self):
        print("Total marks={}".format(self.physics+self.chemistry+self.maths))

s1=Student('shyam','001',80,90,60)#object create time constructor will be called.ie.,__init__ will be called
s1.total_marks()
