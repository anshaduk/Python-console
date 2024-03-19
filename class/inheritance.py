class Vehicle:
    def __init__(self,name,brand,color):
        self.name=name
        self.brand=brand
        self.color=color
    def start_engine(self):
        print("start engine")
    def change_gear(self):
        print("change gear")
class Car(Vehicle):
    def open_roof(self):
        print('Open sunroof')

c1=Car('bmw','x5','black')
c1.change_gear()
c1.open_roof()
c1.start_engine()