class Animal:
    def perform(self):
        print("Animal perform in the circus")

class Human:
    def perform(self):
        print("Human perform in the circus")

class circus:
    def play(self,animal:Animal):
        animal.perform()

tiger=Animal()
anshad=Human()
c1=circus()
c1.play(tiger)
c1.play(anshad)