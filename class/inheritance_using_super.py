class Vehicle:
    def __init__(self,name,brand,color):
        self.name=name
        self.brand=brand
        self.color=color

    def start_engine(self):
        print("starting engine...")
    
    def change_gear(self):
        print("Change gear...")

class Car(Vehicle):
    def __init__(self, name, brand, color,body_type):
        super().__init__(name, brand, color)
        self.body_type=body_type
    def open_roof(self):
        print("open sun roof")

c1=Car('bmw','x5','black','metal')
c1.start_engine()
c1.change_gear()
c1.open_roof()