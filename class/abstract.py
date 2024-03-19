from abc import ABC,abstractmethod
class Vehicle:
    def start_engine(self):
        print("Starting engine..")
    
    def apply_break(self):
        print("Apply break")
    @abstractmethod
    def change_gear(self):
        pass

class Car(Vehicle):
    def open_sunroof(self):
        print("open sunroof")
    def change_gear(self):
        print("Chnage gear automatically")

class Truck(Vehicle):
    def weight_loaded(self):
        print("Weight loaded")
    def change_gear(self):
        print("Change gear manually")

c=Car()
c.change_gear()
t=Truck()
t.change_gear()
