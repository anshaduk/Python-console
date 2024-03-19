
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def __add__(self,other):
        print("Add operator called")
        f_price=self.price+other.price
        print("final price=",f_price)
    
    def __sub__(self,other):
        pass
p1=Product('apple',123)
p2=Product('banana',450)
p1+p2
p1-p2
